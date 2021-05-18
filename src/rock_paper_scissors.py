from enum import IntEnum


class Play(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class WinnerResult(IntEnum):
    Player1 = 0
    Player2 = 1
    Draw = 2


def rock_paper_scissors(play1: Play, play2: Play) -> WinnerResult:
    if play1 == play2:
        return WinnerResult.Draw

    if play1 == Play.Rock and play2 == Play.Scissors:
        return WinnerResult.Player1

    if play1 == Play.Paper and play2 == Play.Rock:
        return WinnerResult.Player1

    if play1 == Play.Scissors and play2 == Play.Paper:
        return WinnerResult.Player1

    return WinnerResult.Player2
