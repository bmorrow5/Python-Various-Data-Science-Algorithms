# Import libraries
from board import Board
from conditional_player import ConditionalPlayer
from argmax import argmax


# Represents a tic-tac-toe agent evaluating moves with a utility function
# Note: this agent inherits from a conditional player
# Note: it uses it's conditional logic for making decisive moves
class UtilityPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
        move = self.get_decisive_move(board)
        if move is not None:
            return move
        else:
            line_utility = self.get_utility_of_lines(board)
            spaces = self.get_utility_of_spaces(board, line_utility)
            best_move = argmax(spaces)
            return best_move
    
        
    def get_utility_of_lines(self, board) -> list:
        line_utilities = []
        lines = board.lines
        for line in lines:
            if self.is_line_empty(board, line):
                utility = 0
            elif self.is_line_full(board, line):
                utility = -10
            else:
                utility = self.get_line_utility(board, line) 
            line_utilities.append(utility)
        return line_utilities 
        
    
    def get_line_utility(self, board, line) -> int:     
        agent_mark = 0
        opponent_marks = 0
        spaces = board.spaces
        
        for space in line:
            if spaces[space] == self.mark:
                agent_mark += 1
            elif spaces[space] == self.opponent_mark:
                opponent_marks += 1
        line_utilities = 3*agent_mark - opponent_marks # Utility Function
        return line_utilities
    
    
    def get_utility_of_spaces(self, board, line_utility) -> list:   
        
        space_utility = []
        for i in range(9):
            space_utility.append(0)

        for i in range(len(line_utility)):
            if i == 0:
                space_utility[0] += line_utility[0]
                space_utility[1] += line_utility[0]
                space_utility[2] += line_utility[0]
            if i == 1:
                space_utility[3] += line_utility[1]
                space_utility[4] += line_utility[1]
                space_utility[5] += line_utility[1]
            if i == 2:
                space_utility[6] += line_utility[2]
                space_utility[7] += line_utility[2]
                space_utility[8] += line_utility[2]
            if i == 3:
                space_utility[0] += line_utility[3]
                space_utility[3] += line_utility[3]
                space_utility[6] += line_utility[3]     
            if i == 4:
                space_utility[1] += line_utility[4]
                space_utility[4] += line_utility[4]
                space_utility[7] += line_utility[4]    
            if i == 5:
                space_utility[2] += line_utility[5]
                space_utility[5] += line_utility[5]
                space_utility[8] += line_utility[5]    
            if i == 6:
                space_utility[0] += line_utility[6]
                space_utility[4] += line_utility[6]
                space_utility[8] += line_utility[6]    
            if i == 7:
                space_utility[2] += line_utility[7]
                space_utility[4] += line_utility[7]
                space_utility[6] += line_utility[7]    

        i=0
        spaces = board.spaces
        for space in spaces:
            if space == "-":
                space_utility[i] += 0
            elif space != "-":
                space_utility[i] = -99
            i += 1
            
        return space_utility 

    # Returns true if the line is empty
    def is_line_empty(self, board, line) -> bool:
       spaces = board.spaces
       for i in range(3):
           if spaces[line[i]] != "-":
               return False
       return True


    # Returns true if the line is full, else false
    def is_line_full(self, board, line) -> bool:
       spaces = board.spaces
       for i in range(3):
           if spaces[line[i]] == "-":
               return False
       return True

