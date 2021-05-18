from unittest import TestCase
from nose2.tools import params
from src.rock_paper_scissors import WinnerResult, Play, rock_paper_scissors


class TestRockPaperScissors(TestCase):
    @params(
        (Play.Rock, Play.Rock, WinnerResult.Draw),
        (Play.Rock, Play.Paper, WinnerResult.Player2),
        (Play.Rock, Play.Scissors, WinnerResult.Player1),
        (Play.Paper, Play.Rock, WinnerResult.Player1),
        (Play.Paper, Play.Paper, WinnerResult.Draw),
        (Play.Paper, Play.Scissors, WinnerResult.Player2),
        (Play.Scissors, Play.Rock, WinnerResult.Player2),
        (Play.Scissors, Play.Paper, WinnerResult.Player1),
        (Play.Scissors, Play.Scissors, WinnerResult.Draw),
    )
    def test_rock_paper_scissors(self, play1: Play, play2: Play, winner: WinnerResult):
        self.assertEqual(
            rock_paper_scissors(play1, play2),
            winner
        )
