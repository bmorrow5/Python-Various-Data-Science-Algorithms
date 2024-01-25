# Import libraries
#from random_player import RandomPlayer
from sequence_player import SequencePlayer
from goal_player import GoalPlayer
from minimax_player import MinimaxPlayer
from human_player import HumanPlayer
from game import Game

# Loop until the user chooses to exit the program
while True:
    # Lets ask the user for the difficulty
    while True:
        try:
            difficulty = int(input("Please Enter the Difficulty: (Easy=1, Medium=2, Hard=3)"))
        except ValueError:
            print("Sorry, I didn't understand that. Please Try again")
            continue
        else:
            break
    if difficulty == 1: 
        player1 = SequencePlayer(1, (0,1,2,3,4,5,6,7,8))
        print("You have selected easy")
    elif difficulty == 2:
        player1 = GoalPlayer(1)
        print("You have selected medium")
    elif difficulty == 3:
        player1 = MinimaxPlayer(1)
        print("You have selected hard")

    player2 = HumanPlayer(2)
    print(f"You are player 2. Your Mark is {player2.mark}")

    # Create a new game using the two players
    game = Game(player1, player2)

    # Play the game to it's conclusion
    game.play()

    # Ask the user if they want to continue
    choice = input("Play another game? Y/N: ")

    # Exit the program if the user doesn't want to play anymore
    if choice != "Y":
        break