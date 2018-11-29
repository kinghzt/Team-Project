player_list = []

# The map can be represented by a simple list of Land, because you only allow players to go forward in a single track
map = []


class Player:
    def __init__(self,name):
        self.name = name
        self.money = 10000
        self.dice_value = 0
        self.location =[0]
        self.inJail = False
        self.ownedLands = []

class Land:           
     def __init__(self, name, price, payment):
        self.name = name
        self.price = price
        self.payment = payment
        self.wasBought = False  
        self.builtHouse = 0         
        self.owner = 'no'


def init_game():
    # print out welcome messages, rules, and initialize map
    # Create the Land object and add them to map

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
    
    pass


def setup_players():
    # prompt users to enter names, and then construct the player list
    # player_list.append[...]

    player_list = []
    number_of_players = int(input("Please enter the number of payers(2-4): "))
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
    # Check whether there is a winner of the game
    return False


def end_game():
    # winner won the game, print out winning status and other messages
    pass


if __name__ == "__main__":
    init_game()
    while check_winner():
        run_game()
    end_game()
