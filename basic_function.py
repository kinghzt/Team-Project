
# -*- coding: utf-8 -*

import random

#intial value of some game functions for Jail, Chance and Max level of building
JAIL_INDEX = 14
CHANCE_EARN_200 = 0
CHANCE_EARN_100 = 1
CHANCE_PAY_200 = 2
CHANCE_PAY_100 = 3
CHANCE_GO_TO_JAIL = 4
CHANCE_BECAME_1000 = 5
MAX_CONSTRUCT_LEVEL = 3

#Ojbect Player
class Player:
    
    # class Player attribute
    def __init__(self,name,money):
        self.name = name
        self.money = money
        self.locatedLand = 0
        self.inJail = False
        self.JailedRound = 0
        self.isBroke = False
        self.owned_land = []
 
    #Payment function
    def payMoney(self, amount):
        if amount > self.money:
            self.isBroke = True
            print('Player {} has became impoverished and out of game!!!'.format(self.name))
            return False
        else:
            self.money -= amount
            return True
    #Salary function
    def earnMoney(self, amount):
        self.money += amount
        return self.money
    #Chance room function
    def money_1000(self):
        self.money = 1000
        return self.money
    #Showing current player's balance and land properties
    def displayProperties(self):
        print('Player {}\'s balance: {} with the following land properties:\n'.format(self.name, self.money))
        for land in self.owned_land:
            print(land.name, end=' ')
        print('\n')

#Class Land
class Land:
    def __init__(self, name,price,constructionCost):
        self.name = name
        self.basicPrice = price
        self.basicConstructionCost = constructionCost 
        self.constructionLevel = 0
        self.owner = None
    #Dynamiclly chaning the construction cost
    def queryConstructCost(self):
 
        return self.basicConstructionCost * (self.constructionLevel + 1)
    #one of the main functions of building house
    def construct(self, player):
        print('Player {} has constructed a house at {}'.format(player.name,self.name))
        self.owner = player
        player.owned_land.append(self)
        player.payMoney(self.basicPrice)
        self.constructionLevel += 1
    #one of the main functions of upgrading house level
    def upgrade(self):
        print('Upgrade house at {} from {} to {}'.format(self.name,self.constructionLevel,self.constructionLevel+1))
        self.owner.payMoney(self.queryConstructCost())
        self.constructionLevel += 1
    #Setting house level
    def queryLevel(self):
        return self.constructionLevel
    #Setting Toll Fee dynamiclly
    def queryRoadToll(self):

       	return 0.4*self.basicPrice*(2 * self.constructionLevel + 1)

#Class Map
class Map:
    #Initial attribute of Map
    def __init__(self):
        #Setting basic value of each place
        self.board = [
                Land('Go',0,0),
                Land('LIBYA', 50,10),
                Land('SUDAN',60,12),
                Land('MOROCCO',70,14),
                Land('TURKEY',100,20),
                Land('GREECE',110,22),
                Land('BULGARIA',120,24),
                Land('CHANCE',0,0),
                Land('POLAND',160,32),
                Land('RUSSIA',170,34),
                Land('UKRAINE',180,36),
                Land('LITHUANIA',200,40),
                Land('LATVIA',210,42),
                Land('ESTONIA',220,44),
                Land('JAIL',0,0),
                Land('NORWAY',220,44),
                Land('SWEDEN',230,46),
                Land('FINLAND',240,48),
                Land('GERMANY',280,56),
                Land('FRANCE',290,58),
                Land('UNITED KINDOM',300,60),
                Land('CHANCE',0,0),
                Land('CANADA',300,60),
                Land('MEXICO',310,62),
                Land('USA',320,64),
                Land('CHINA ',330,66),
                Land('DUBAI ',360,72),
                Land('HAWAII',400,80)]

    def getLength(self):
        return len(self.board)

    def getLand(self, index):
        return self.board[index]


class Game:

    def __init__(self):
        self.map = Map()
        self.players = []
        self.playTurn = 0
        self.remainPlayer = -1
        self.numPlayer = -1

    def initialGame(self):
        print("*"*50)
        print("*" * 50)
        print(" " * 10 + "Game of Monopoly! Enjoy your time!" + " "*10)
        print("*" * 50)
        print("*" * 50)


        number_of_players = int(input("Please enter the number of payers(2-4): "))

        while number_of_players <2 or number_of_players >4:
            number_of_players = int(input("Sorry, the current version cannot support this mode. \n Please enter the  correct number of payers(2-4): "))

        self.numPlayer = number_of_players
        self.remainPlayer = number_of_players

        money = int(input('Please Enter the initial amount of money that you would like to play:  '))
     
        for i in range(0,number_of_players):
            player_name = input("Enter the Player name:")
            while player_name =='':
                player_name = input("You must have a valid name to start. Please Enter the Player name: ")
            self.players.append(Player(player_name,money))

        
        print('\n\n\n\n')

    def start(self):
        while(True):
            if self.remainPlayer == 1:
                self.endGame()
                break
            else:
                if self.players[self.playTurn].isBroke:
                    pass
                else:
                    print('It is {}\'s turn to go'.format(self.players[self.playTurn].name))
                    input('Please Enter any Key to Throw a Dice:')
    

                    print('{} is throwing a dice'.format(self.players[self.playTurn].name))
                    step = self.rollDice()
                    print('You get {}'.format(step))
                    if self.players[self.playTurn].inJail:
                        print('Player {} is in Jail'.format(self.players[self.playTurn].name))
                        self.players[self.playTurn].JailedRound += 1
                        if  self.players[self.playTurn].JailedRound == 3 or step==6:
                            self.players[self.playTurn].JailedRound = 0
                            self.players[self.playTurn].inJail = False
                        if step == 6:
                            continue
                    else:
                        
                        print('You can go {} steps forward'.format(step))
                        player = self.players[self.playTurn]
    
                        if player.locatedLand+step>=self.map.getLength():
                            player.earnMoney(200)
                            print('Passing the start point. You earn $200')
                        player.locatedLand = (step + player.locatedLand)%self.map.getLength()
    
                        curLand = self.map.getLand(player.locatedLand)
                        print('Player {} is at {}'.format(player.name, curLand.name))
                        self.landOperation(curLand, player)
                    player.displayProperties()
                    input('Please Enter any Key to End this round: ')
                print('\n'*3)
                self.playTurn = (self.playTurn + 1)% self.numPlayer
                self.updateRemainPlayer()

    def landOperation(self, curLand, player):
        print('You current money is ${}'.format(player.money))
        if curLand.name == 'CHANCE':
            self.doChance(player)
        elif curLand.name == 'JAIL':
                player.inJail = True
        elif curLand.name == 'Go':
            pass
        elif curLand.owner == None:
            if player.money >= curLand.basicPrice:
                while True:
                    choice  = str(input('Land cost is  ${}.  \nAre you willing to buy this land(Y/N)?:  '.format(curLand.basicPrice)))
                    if choice == 'Y' or choice == 'y':
                        curLand.construct(player)
                        break
                    elif choice == 'N' or choice == 'n':
                        break
                    else:
                        print('Please input valid choice')
            else:
                print("Your current balance is not enough to buy this land!")
        elif curLand.owner == player:
            if curLand.constructionLevel!=MAX_CONSTRUCT_LEVEL and player.money >= curLand.queryConstructCost():
                while True:
                    choice  = str(input('Construction cost is  ${}. \nAre you willing to upgrade this house(Y/N)?:  '.format(curLand.queryConstructCost())))
                    if choice == 'Y' or choice == 'y':
                        curLand.upgrade()
                        break
                    elif choice == 'N' or choice == 'n':
                        break
                    else:
                        print('Please input valid choice')
        else:
            paid_amount = min(curLand.queryRoadToll(), player.money)
            curLand.owner.earnMoney(paid_amount)
            print('{} paid ${} to {}'.format(player.name, paid_amount, curLand.owner.name))
            player.payMoney(curLand.queryRoadToll()) 


    def rollDice(self):
        return random.randint(1, 6)


    def doChance(self, player):
        chance_code = random.randint(0,5)
        print('Player {} get a dice value of {}'.format(player.name,chance_code))
        if chance_code == CHANCE_EARN_100:
            print('Player' + player.name + 'just Won $100 from Chance room!')
            player.earnMoney(100)
        elif chance_code == CHANCE_EARN_200:
            print('Player' + player.name + 'just Won $200 from Chance room!')
            player.earnMoney(200)
        elif chance_code == CHANCE_PAY_100:
            print('Player' + player.name + 'just lost $100 from Chance room!')
            
            player.payMoney(100)
        elif chance_code == CHANCE_PAY_200:
            print('Player' + player.name + 'just lost $200 from Chance room!')
            player.payMoney(200)
        elif chance_code == CHANCE_BECAME_1000:
            print('Player' + player.name + 'total amount of money became $1000')
            player.money_1000()
            
        elif chance_code == CHANCE_GO_TO_JAIL:
            print("Player {} are under arrested! You have stay here in the next three turns unless you can get a dice value of 6".format(player.name))
            player.inJail = True
            player.locatedLand = JAIL_INDEX
        else:
            pass

    def getSurvivior(self):
        ret = []
        for player in self.players:
            if not player.isBroke:
                ret.append(player)
        return ret 

    def updateRemainPlayer(self):
        ret = 0
        for player in self.players:
            if not player.isBroke:
                ret+=1
        self.remainPlayer = ret

    def endGame(self):
 
        print("*" * 100)
        print("*" * 100)
        print('■                                ■                                ■       ■          ■■                           ■')
        print('  ■                            ■  ■                             ■         ■          ■    ■                       ■')
        print('   ■                         ■      ■                         ■           ■          ■       ■                    ■')
        print('     ■                     ■          ■                     ■             ■          ■          ■                 ■')
        print('       ■                 ■              ■                 ■               ■          ■             ■              ■')
        print('         ■             ■                  ■             ■                 ■          ■                ■           ■')
        print('           ■         ■                      ■         ■                   ■          ■                   ■        ■')
        print('             ■     ■                          ■     ■                     ■          ■                      ■     ■')
        print('               ■ ■                              ■ ■                       ■          ■                         ■  ■')
        print('                ■                                ■                        ■          ■                           ■■')
        print("*" * 100)
        print("*" * 100)
        print('Player {} is the winner'.format(self.getSurvivior()[0].name))


if __name__ == "__main__":
    game = Game()
    game.initialGame()
    from PIL import Image
    im = Image.open('Monopoly.jpg')
    im.show()
    game.start()
-
