from nest.core import Controller, Get, Post, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config import config


from .leaderboard_service import LeaderboardService
from .leaderboard_model import Leaderboard, LeaderboardResponse


@Controller("leaderboard")
class LeaderboardController:
    service: LeaderboardService = Depends(LeaderboardService)

    @Get("/raw")
    async def get_leaderboard_raw(
        self, session: AsyncSession = Depends(config.get_db), days: int = 1
    ):
        return await self.service.get_leaderboard_raw(session, days)

    @Get("/", response_model=LeaderboardResponse)
    async def get_leaderboard(
        self, session: AsyncSession = Depends(config.get_db), days: int = 1
    ):
        return await self.service.get_leaderboard_data(session, days)

    @Post("/")
    async def add_leaderboard(
        self, leaderboard: Leaderboard, session: AsyncSession = Depends(config.get_db)
    ):
        return await self.service.add_leaderboard(leaderboard, session)
