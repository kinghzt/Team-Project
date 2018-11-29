import PIL
import random

player_list = []
# The map can be represented by a simple list of Land, because you only allow players to go forward in a single track
board = []
#initial game status
game_running = True

class Player:
    def __init__(self,name):
        self.name = name
        self.money = 10000
        self.dice_value = 0
        self.locatedLand = 0
        self.inJail = False
        self.ownedLands = []
        self.enterYes = 'no'

    def move(self):
        if self.inJail == True:
            count = 0
            print("You are still in Jail. You have to get a dice value of 6 to get you out of Jail")
            
            self.dice_value=random.randint(1,7)
            if self.dice_value == 6 or count == 3:
                  print("Ok. You are free now")
                  
                  self.dice_value=random.randint(1,7)
                  temp =self.locatedLand.location+ self.dice_value
                  if temp >= 28:
                      temp -= 28
                  self.locatedLand=board[temp]
            else:
                count = count + 1
                print('You cannot get out of Jail now')
        else:

            self.dice_value=random.randint(1,7)          
            temp =self.locatedLand.location+ self.dice_value
            if temp >= 28:
                temp -= 28
            self.locatedLand=board[temp]

    def buyaLand(self): 
        if  self.enterYes== 'yes' and self.locatedLand.owner != self.name:
            self.locatedLand.owner = self.name
            self.locatedLand.wasBought = True
            self.ownedLands.append(self.locatedLand)
            self.money -= self.locatedLand.price
            print(self.name + 'bought' + self.locatedLand.name + '!')
            return True
        else:
            None
    
    def construction(self):
        if  self.enterYes== 'yes' and self.locatedLand.owner != self.name:
            self.locatedLand.constructionLevel+= 1
            self.money -= self.locatedLand.constructionCost
            print(self.name + 'built a hotel on' + self.locatedLand.name)
            return True
        else:
            None
    
    def event(self, player_list): 
        Land == self.locatedLand
        
        if Land.name == 'CHANCE':
            print("Welcome come to the Chance room! Let's see if you a lucky dog or not")

            chance_incident = ['+$200', '+$100', '-$100','-$200','Jail','equal_to_1000']
            get_chance = random.choice(chance_incident)

            if get_chance == '+$200':
                self.money = self.money + 200
                print('Player' + self.name + 'just Won $200 from Chance room!')
            elif get_chance == '+$100':
                self.money = self.money + 100
                print('Player' + self.name + 'just Won $100 from Chance room!')
            elif get_chance == '-$100':
                self.money = self.money - 100
                print('Player' + self.name + 'just lost $100 from Chance room!')
            elif get_chance == '-$200':
                self.money = self.money - 200
                print('Player' + self.name + 'just lost $200 from Chance room!')
            elif get_chance == 'Jail':
                self.locatedLand = 14
                self.inJail = True
                print('Player' + self.name + 'is sent to Jail because of bad luck')
            elif get_chance == 'equal_to_1000':
                self.money = 1000
                print('Player' + self.name + 'total amount of money became $1000')
            
        if Land.name == 'Jail':
            print("You are under arrested! You have stay here in the next three turns unless you can get a dice value of 6")
            self.inJail = True
            
            pass

        else:
            if Land.wasBought == False:     
                print(self.name +'threw a' + '%d'% self.dice_value + 'on the dice!')
                print(self.name +'is in' + Land.name + '!')
                print('Buying price is %d' % Land.price)
                enterYes=input("Whether to buy?(yes/no): ")
                while enterYes != 'yes' and enterYes != 'no':
                    enterYes = input("You must enter yes or no. Please Enter Your Choice: ")
                    return self.buyaland()
            elif Land.owner == self.name:
                print(self.name + 'threw a' + '%d'% self.dice_value + 'on the dice,')
                print(self.name + 'comes to his land:'+ Land.name +'!')
                if Land.constructionLevel <2:
                    print('You can built a hotel on your land!')
                    print('Construction fee is %d'% Land.constructionCost)
                    enterYes=input("Whether to build?(yes/no): ")
                    while enterYes != 'yes' and enterYes != 'no':
                        enterYes = input("You must enter yes or no. Please Enter Your Choice: ")
                    return self.construction()
                else:
                    print('You have reached its maximum level.')
            else:
                for player in player_list:
                    if Land.owner == player.name and player.name != self.name:
                        print(self.name + 'threw a' + '%d'% self.dice_value + 'on the dice!')
                        print(self.name+ 'comes to'+ player.name+ 'land.')
                        print('You are being charged!')
                        print('Passing fee is %d' % (0.4 * Land.price * (2* Land.constructionLevel +1)))
                        self.money -= 0.4 * Land.price * (2* Land.constructionLevel +1)
                        player.money += 0.4 * Land.price * (2* Land.constructionLevel +1)
                    else:

                        None
    def broke(self):
        if self.money < 0:
            print('You are broke. Game ends')
            player_list.remove(self.name)
            for land in self.ownedLands:
                land.owner = 'no'
                land.wasBought = False
                land.constructionLevel = 0
        else:
            None
class Land:
    def __init__(self, name, price, location, constructionCost):
        self.name = name
        self.price = price
        self.constructionCost = constructionCost
        self.wasBought = False  
        self.constructionLevel = 0
        self.location = location
        self.owner = 'no'                                                                                                                                                                                                            
            
def init_game():
    # print out welcome messages, rules, and initialize map
    #Create the Land object and add them to map
    print("*"*50)
    print("*" * 50)
    print(" " * 10 + "Game of Monopoly! Enjoy your time!" + " "*10)
    print("*" * 50)
    print("*" * 50)

    setup_players()
    #Create Lands Object
    start = Land('Go',-200,0,0)
    land1 = Land('LIBYA', 50,1,10)
    land2 = Land('SUDAN',60,2,12)
    land3 = Land('MOROCCO',70,3,14)
    land4 = Land('TURKEY',100,4,20)
    land5 = Land('GREECE',110,5,22)
    land6 = Land('BULGARIA',120,6,24)
    land7 = Land('CHANCE',0,7,0)
    land8 = Land('POLAND',160,8,32)
    land9 = Land('RUSSIA',170,9,34)
    land10 = Land('UKRAINE',180,10,36)
    land11 = Land('LITHUANIA',200,11,40)
    land12 = Land('LATVIA',210,12,42)
    land13 = Land('ESTONIA',220,13,44)
    land14 = Land('JAIL',0,14,0)
    land15 = Land('NORWAY',220,15,44)
    land16 = Land('SWEDEN',230,16,46)
    land17 = Land('FINLAND',240,17,48)
    land18 = Land('GERMANY',280,18,56)
    land19 = Land('FRANCE',290,19,58)
    land20 = Land('UNITED KINDOM',300,20,60)
    land21 = Land('CHANCE',0,21,0)
    land22 = Land('CANDA',300,22,60)
    land23 = Land('MEXICO',310,23,62)
    land24 = Land('USA',320,24,64)
    land25 = Land('CHINA ',330,25,66)
    land26 = Land('DUBAI ',360,26,72)
    land27 = Land('HAWAII',400,27,80)
    board=[start, land1, land2, land3, land4, land5, land6, land7, land8, land9, land10, land11, land12, land13, land14, land15, land16, land17, land18, land19, land20, land21, land22, land23, land24, land25, land26, land27]
    
    from PIL import Image
    im = Image.open('Monopoly.jpeg')
    im.show()

    pass


def setup_players():
    # prompt users to enter names, and then construct the player list
    # player_list.append[...]

    player_list = []
    number_of_players = int(input("Please enter the number of payers(2-4): "))
    while number_of_players <2 or number_of_players >4:
        number_of_players = int(input("Sorry, the current version cannot support this mode. \n Please enter the  correct number of payers(2-4): "))
    for i in range(0,number_of_players):
        player_name = input("Enter the Player name:")
        while player_name =='':
            player_name = input("You must have a valid name to start. Please Enter the Player name: ")
        player_list.append(Player(player_name))
    
    return player_list
    pass


def run_game():
    # e.g.:
    # while (some conditions that you determine to end a round):
    #   play_round()

        
        
    pass


def play_round():
    # Each player tosses the dice and make the move
    # Make sure to update the Player object
    pass


def check_winner():
    print(winner.name,"is the wineer!")
    return False


def end_game():
    # winner won the game, print out winning status and other messages
    pass


if __name__ == "__main__":
    init_game()
    while check_winner():
        run_game()
    end_game()

