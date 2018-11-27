class basic_function():
    def game_start(self):
        
        print("*"*50)
        print("*" * 50)
        print(" " * 10 + "Game of Monopoly! Enjoy your time!" + " "*10)
        print("*" * 50)
        print("*" * 50)
    def input_name(self):
        player_name = input("Enter the Player name: ")
        while player_name == '':
            player_name = input("You must have a name to start. Please Enter the Player name: ")
        print(player_name)
        return player_name

    def win(self,winner):
        print(f"{winner} is the winner!")

