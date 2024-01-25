# Import libraries
from player import Player
from board import Board


# Represents a tic-tac-toe agent that evaluates moves using conditional logic
class ConditionalPlayer(Player):

    # Returns the next move given the current board state
    def get_next_move(self, board) -> int:
        move = self.get_decisive_move(board)
        if move is not None:
            return move
        else:
            return self.get_non_decisive_move(board)
                
    # Returns the next move that will result in victory
    # This function checks the win conditions
    def get_decisive_move(self, board):
        
        # Lets create new instances of the board and check for winning cases
        spaces = board.get_open_spaces()
        #First loop checks if player1 has winning case
        for space in spaces:
            board_copy = board.copy()
            board_copy.mark_space(space, self.mark)
            if board_copy.has_win(self.mark):
                return space

        # Now check player 2 for winning case
        for space in spaces:
            board_copy2 = board.copy()
            board_copy2.mark_space(space, self.opponent_mark)
            if board_copy2.has_win(self.opponent_mark):
                return space
        return None


        # If no decisive move exists (mirrored the test case sequence)
    def get_non_decisive_move(self, board):
        
        if board.is_open_space(0):
            return 0
        elif board.is_open_space(4):
            return 4
        elif board.is_open_space(2):
            return 2
        elif board.is_open_space(6):
            return 6
        elif board.is_open_space(8):
            return 8
        elif board.is_open_space(1):
            return 1
        elif board.is_open_space(3):
            return 3
        elif board.is_open_space(5):
            return 5
        elif board.is_open_space(7):
            return 7
        else:
            return None