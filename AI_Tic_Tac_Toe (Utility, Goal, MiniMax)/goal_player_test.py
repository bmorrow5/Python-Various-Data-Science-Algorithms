import unittest
from parameterized import parameterized
from goal_player import GoalPlayer
from board import Board


class GoalPlayerTests(unittest.TestCase):
    @parameterized.expand([
        ["---------", 4],
        ["X--------", 4],
        ["OX-X-----", 4],
        ["X-X------", 1],

    ])
    def test_get_next_move(self, state, expected_move):
        board = Board(state)
        player = GoalPlayer(2)
        result = player.get_next_move(board)
        self.assertEqual(expected_move, result)

    @parameterized.expand([
        ["XX-------", 'win'],
        ["-XX------", 'win'],
        ["---XX----", 'win'],
        ["----XX---", 'win'],
        ["------XX-", 'win'],
        ["-------XX", 'win'],
        ["X-------X", 'win'],
        ["--X---X--", 'win'],
        ["X--X-----", 'win'],
        ["-X--X----", 'win'],
        ["--X--X---", 'win'],
        ["------X-X", 'win'],
        ["---X-X---", 'win'],
        ["X-X------", 'win'],
        ["OO-------", 'block'],
        ["-OO------", 'block'],
        ["---OO----", 'block'],
        ["----OO---", 'block'],
        ["------OO-", 'block'],
        ["-------OO", 'block'],
        ["O-------O", 'block'],
        ["--O---O--", 'block'],
        ["O--O-----", 'block'],
        ["-O--O----", 'block'],
        ["--O--O---", 'block'],
        ["------O-O", 'block'],
        ["---O-O---", 'block'],
        ["O-O------", 'block'],
        ["--O------", 'take center'],
        ["-O-------", 'take center'],
        ["-O-------", 'take center'],
        ["----X---O", 'get top left'],
        ["----X-O--", 'get top right'],
        ["--O-X----", 'get bottom left'],
        ["O---X----", 'get bottom right'],
        
    ])
    def test_get_goal(self, state, expected):
        board = Board(state)
        player = GoalPlayer(1)
        result = player.get_goal(board)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["---X-X---", 'win', 4],
        ["X-X------", 'win', 1],
        ["OO-------", 'block',2],
        ["-OO------", 'block',0],
        ["--O------", 'take center',4],
        ["-O-------", 'take center',4],
        ["-O-------", 'take center',4],
        ["----X---O", 'get top left',0],
        ["----X-O--", 'get top right',2],
        ["--O-X----", 'get bottom left',6],
        ["O---X----", 'get bottom right',8],

    ])
    def test_get_goal_move(self, state, goal, expected):
        board = Board(state)
        player = GoalPlayer(1)
        result = player.get_goal_move(board, goal)
        self.assertEqual(expected, result)
    
    @parameterized.expand([
        ["XX-------", [2,3,4,5,6,7,8], 'win'],
        ["O--O-----", [1,2,4,5,6,7,8], 'block'],
    ])
    
    def test_check_win_or_block_goal(self, state, open_spaces, expected):
        board = Board(state)
        player = GoalPlayer(1)
        result = player.check_win_or_block_goal(board, open_spaces)
        self.assertEqual(expected, result)

    
if __name__ == '__main__':
    unittest.main()