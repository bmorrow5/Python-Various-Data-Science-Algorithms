# Import libraries
from board import Board
from conditional_player import ConditionalPlayer

# Represents a tic-tac-toe goal based agent
# Note: this agent inherits from a conditional player
# Note: This class reads the board to determine its goal and then 
# based on this goal determines the move to make
class GoalPlayer(ConditionalPlayer):

    # Gets the next move using an utility function
    # and conditional logic for decisive moves
    def get_next_move(self, board: Board) -> int:
            goal = self.get_goal(board)
            move = self.get_goal_move(board, goal)
            return move
    
    # Identifies which goal needs to be accomplished by reading the board
    def get_goal(self, board) -> str:
        
        spaces = board.spaces
        agent_marks = []
        opponent_marks = []
        
        # Create lists from the marks
        for i in range(9):
            if spaces[i] == self.mark:
                agent_marks.append(i)
            elif spaces[i] == self.opponent_mark:
                opponent_marks.append(i)
        
        open_spaces = board.get_open_spaces()
        win_or_block = self.check_win_or_block_goal(board, open_spaces)
        if win_or_block == 'win':
            return 'win'
        elif win_or_block == 'block':
            return 'block'
        
        #Check if center open
        if 4 not in opponent_marks and 4 not in agent_marks:
                return 'take center' 
        elif 4 not in agent_marks:
            if 4 not in opponent_marks:
                return 'take center' 
        
        # Take corner move
        if 0 in opponent_marks and 8 in open_spaces:
                return 'get bottom right'   
        if 2 in opponent_marks and 6 in open_spaces:
                return 'get bottom left'
        if 6 in opponent_marks and 2 in open_spaces:
                return 'get top right'        
        if 8 in opponent_marks and 0 in open_spaces:
                return 'get top left'
        return 'get side'
        
        
    # Based on the goal determines the necessary move   
    def get_goal_move(self, board, goal) -> int:      
        if goal == 'win':
            move = self.get_decisive_move(board)
            return move
        elif goal == 'block':
            move = self.get_decisive_move(board)
            return move
        elif goal == 'take center':
            return 4
        elif goal == 'get top left':
            return 0
        elif goal == 'get top right':
            return 2
        elif goal == 'get bottom left':
            return 6
        elif goal == 'get bottom right':
            return 8
        elif goal == 'get side':
            open_spaces = board.get_open_spaces()
            return open_spaces[0]
        
        
    def check_win_or_block_goal(self, board, open_spaces) -> str:
        # Check win
        for open_space in open_spaces:
            board_copy = board.copy()
            board_copy.mark_space(open_space, self.mark)
            if board_copy.has_win(self.mark):
                return 'win'
            
        # Check block
        for open_space in open_spaces:
            board_copy1 = board.copy()
            board_copy1.mark_space(open_space, self.opponent_mark)
            if board_copy1.has_win(self.opponent_mark):
                return 'block'
        

