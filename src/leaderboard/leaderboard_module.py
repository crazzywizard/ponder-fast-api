from .leaderboard_service import LeaderboardService
from .leaderboard_controller import LeaderboardController


class LeaderboardModule:

    def __init__(self):
        self.providers = [LeaderboardService]
        self.controllers = [LeaderboardController]
