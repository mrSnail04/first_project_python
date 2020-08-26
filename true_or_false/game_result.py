from dataclasses import dataclass


@dataclass
class GameResult:
    questions_passed: int
    mistake_made: int
    won: bool