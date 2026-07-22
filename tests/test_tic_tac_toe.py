import unittest
from unittest.mock import patch

from tic_tac_toe import check_draw, check_winner, get_move, switch_player


class TicTacToeTests(unittest.TestCase):
    def test_check_winner_detects_a_row(self):
        board = ["X", "X", "X", " ", " ", " ", " ", " ", " "]
        self.assertEqual(check_winner(board), "X")

    def test_check_winner_returns_none_for_incomplete_board(self):
        board = ["X", "O", " ", " ", " ", " ", " ", " ", " "]
        self.assertIsNone(check_winner(board))

    def test_check_draw_detects_full_board(self):
        board = ["X", "O", "X", "X", "O", "O", "O", "X", "X"]
        self.assertTrue(check_draw(board))

    def test_switch_player_alternates(self):
        self.assertEqual(switch_player("X"), "O")
        self.assertEqual(switch_player("O"), "X")

    def test_get_move_retries_invalid_and_taken_positions(self):
        board = ["X", " ", " ", " ", " ", " ", " ", " ", " "]

        with patch("builtins.input", side_effect=["0", "2"]):
            index = get_move(board, "O")

        self.assertEqual(index, 1)


if __name__ == "__main__":
    unittest.main()
