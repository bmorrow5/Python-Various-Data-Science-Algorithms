# Import libraries
from player import Player
from board import Board
from argmax import argmax


# Represents a brute-force minimax agent
class MinimaxPlayer(Player):

    # Initialize the player
    def __init__(self, player_number):
        super().__init__(player_number)

    # Returns the next move given the current board state
    def get_next_move(self, board: Board) -> int:
        _, best_move = self.get_minimax(board, True) # Get the best (max) move
        return best_move

    # Recursively determine the best move for the current player 
    # I opted to go with one function to match the unit test, but could split into max and min value functions
    # The only modification to the test file is adding results[0] to only get the best move value
    def get_minimax(self, state: Board, is_max: bool):
        if state.has_win(self.mark) or state.has_win(self.opponent_mark) or state.is_full():
            return self.get_score(state), None
        else:
            if is_max: # Max_Value
                v = -10
                best_move = None
                for space in state.get_open_spaces():
                    next_state = state.copy()
                    next_state.mark_space(space, self.mark)
                    v2, _ = self.get_minimax(next_state, False)
                    if v2 > v:
                        v, best_move = v2, space
                return v, best_move
            else: # Min_Value
                v = 10 
                best_move = None
                for space in state.get_open_spaces():
                    next_state = state.copy()
                    next_state.mark_space(space, self.opponent_mark)
                    v2, _ = self.get_minimax(next_state, True) 
                    if v2 < v:
                        v, best_move = v2, space
                return v, best_move

    # Returns the score for the given board state
    def get_score(self, state: Board):
        if state.has_win(self.mark):
            return 10
        elif state.has_win(self.opponent_mark):
            return -10
        else:
            return 0
