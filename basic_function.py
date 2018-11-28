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
