import random
JAIL_INDEX = 14
CHANCE_EARN_200 = 0
CHANCE_EARN_100 = 1
CHANCE_PAY_200 = 2
CHANCE_PAY_100 = 3
CHANCE_GO_TO_JAIL = 4
MAX_CONSTRUCT_LEVEL = 3
class Player:
    def __init__(self,name):
        self.name = name
        self.money = 10000
        self.locatedLand = 0
        self.inJail = False
        self.JailedRound = 0
        self.isBroke = False
    def payMoney(self, amount):
        if amount > self.money:
            self.isBroke = True
            print('Player {} is broke!'.format(self.name))
            return False
        else:
            self.money -= amount
            return True
    def earnMoney(self, amount):
        self.money += amount

class Land:
    def __init__(self, name, price, constructionCost):
        self.name = name
        self.basicPrice = price
        self.basicConstructionCost = constructionCost 
        self.constructionLevel = 0
        self.owner = None
    def queryConstructCost(self):
        #You should define your construction fee rule here
        return self.basicConstructionCost * (self.constructionLevel + 1)
    def construct(self, player):
        print('Build house at {}'.format(self.name))
        self.owner = player
        player.payMoney(self.queryConstructCost())
        self.constructionLevel += 1
    def upgrade(self):
        print('Upgrade house at {} from {} to {}'.format(self.name,self.constructionLevel,self.constructionLevel+1))
        self.owner.payMoney(self.queryConstructCost())
        self.constructionLevel += 1
    def queryLevel(self):
        return self.constructionLevel
    def queryRoadToll(self):
        #You should define your road toll rule here
        return self.basicPrice*self.constructionLevel

class Map:
    def __init__(self):
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
                Land('CANDA',300,60),
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
        number_of_players = int(input("Please enter the number of players(2-4): "))
        while number_of_players <2 or number_of_players >4:
            number_of_players = int(input("Sorry, the current version cannot support this mode. \n Please enter the  correct number of payers(2-4): "))
        self.numPlayer = number_of_players
        self.remainPlayer = number_of_players
        for i in range(0,number_of_players):
            player_name = input("Enter the Player name:")
            while player_name =='':
                player_name = input("You must have a valid name to start. Please Enter the Player name: ")
            self.players.append(Player(player_name))

    def start(self):
        while(True):
            if self.remainPlayer == 1:
                self.endGame()
                break
            else:
                print('It is {}\'s turn to go'.format(self.players[self.playTurn].name))
                if self.players[self.playTurn].inJail:
                    print('Player {} is in Jail'.format(self.players[self.playTurn].name))
                    self.players[self.playTurn].JailedRound += 1
                    if  self.players[self.playTurn].JailedRound == 3:
                        self.players[self.playTurn].JailedRound = 0
                        self.players[self.playTurn].inJail = False
                elif self.players[self.playTurn].isBroke:
                    pass
                else:
                    step = self.rollDice()
                    print('You can go {} steps forward'.format(step))
                    player = self.players[self.playTurn]
                    if player.locatedLand+step>=self.map.getLength():
                        player.earnMoney(200)
                        print('Passing the start point. You earn 200')
                    player.locatedLand = (step + player.locatedLand)%self.map.getLength()
                    curLand = self.map.getLand(player.locatedLand)
                    print('Player {} is at {}'.format(player.name, curLand.name))
                    self.landOperation(curLand, player)
                print('\n'*3)
                self.playTurn = (self.playTurn + 1)% self.numPlayer
                self.updateRemainPlayer()
    def landOperation(self, curLand, player):
        if curLand.name == 'CHANCE':
            self.doChance(player)
        elif curLand.name == 'JAIL':
                player.inJail = True
        elif curLand.name == 'Go':
            pass
        elif curLand.owner == None:
            if player.money >= curLand.queryConstructCost():
                while True:
                    choice  = str(input('Are you willing to buy this land(Y/N)？ cost ${}'.format(curLand.queryConstructCost())))
                    if choice == 'Y' or choice == 'y':
                        curLand.construct(player)
                        break
                    elif choice == 'N' or choice == 'n':
                        break
                    else:
                        print('Please input valid choice')
        elif curLand.owner == player:
            if curLand.constructionLevel!=MAX_CONSTRUCT_LEVEL and player.money >= curLand.queryConstructCost():
                while True:
                    choice  = str(input('Are you willing to upgrade this house(Y/N)？ cost ${}'.format(curLand.queryConstructCost())))
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
            player.payMoney(curLand.queryRoadToll()) 
            print('{} paid {} to {}'.format(player.name, paid_amount, curLand.owner.name))
    def rollDice(self):
        return random.randint(1, 6)
    def doChance(self, player):
        chance_code = random.randint(0,4)
        if chance_code == CHANCE_EARN_100:
            player.earnMoney(100)
        elif chance_code == CHANCE_EARN_200:
            player.earnMoney(200)
        elif chance_code == CHANCE_PAY_100:
            player.payMoney(100)
        elif chance_code == CHANCE_PAY_200:
            player.payMoney(200)
        elif chance_code == CHANCE_GO_TO_JAIL:
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
    def endGame(self, player):
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
        print('Player {} is the winner'.format(self.getSurvivior[0].name))
if __name__ == "__main__":
    game = Game()
    game.initialGame()
    from PIL import Image
    im = Image.open('Monopoly.jpg')
    im.show()
    game.start()
