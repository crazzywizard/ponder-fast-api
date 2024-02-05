import collections
from functools import reduce
from .leaderboard_model import Leaderboard
from .leaderboard_entity import Leaderboard as LeaderboardEntity
from nest.core.decorators import async_db_request_handler
import datetime
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class LeaderboardService:
    @async_db_request_handler
    async def add_leaderboard(self, leaderboard: Leaderboard, session: AsyncSession):
        new_leaderboard = LeaderboardEntity(**leaderboard.dict())
        session.add(new_leaderboard)
        await session.commit()
        return new_leaderboard.id

    @async_db_request_handler
    async def get_leaderboard_raw(self, session: AsyncSession, days: int = 1):
        time_24_hours_ago = datetime.datetime.now() - datetime.timedelta(days=days)
        query = select(LeaderboardEntity).filter(
            LeaderboardEntity.timestamp >= time_24_hours_ago.timestamp()
        )
        result = await session.execute(query)
        return result.scalars().all()

    @async_db_request_handler
    async def get_leaderboard_data(self, session: AsyncSession, days: int = 1):
        chains = [
            {
                "id": 1,
                "key": "mainnetReward",
            },
            {
                "id": 10,
                "key": "optimismReward",
            },
            {
                "id": 8453,
                "key": "baseReward",
            },
            {
                "id": 7777777,
                "key": "zoraReward",
            },
        ]
        data_time_range = datetime.datetime.now() - datetime.timedelta(days=days)
        query = select(LeaderboardEntity).filter(
            LeaderboardEntity.timestamp >= data_time_range.timestamp()
        )
        result = await session.execute(query)
        allData = result.scalars().all()
        allData = [d.__dict__ for d in allData]
        allData = [{**d, "rewardType": f'{d["chain"]}Reward'} for d in allData]

        default_rewards = {
            "totalCreatorReward": 0,
        }

        for chain in chains:
            default_rewards[chain["key"]] = 0

        (
            grouped_data,
            total_zora_fees,
            total_creator_fees,
        ) = get_grouped_data(allData, default_rewards)

        leaderboard_data = generate_leaderboard_data(grouped_data, chains)

        return {
            "leaderboard_data": leaderboard_data,
            "recordsCount": len(allData),
            "totalZoraFees": str(total_zora_fees),
            "totalCreatorFees": str(total_creator_fees),
        }


def get_grouped_data(allData: dict, default_rewards: dict):
    total_zora_fees = 0
    total_creator_fees = 0
    grouped_data = collections.defaultdict(lambda: default_rewards.copy())

    for curr in allData:
        recipients_and_fees = zip(
            (
                curr["creator"],
                curr["createReferral"],
                curr["firstMinter"],
                curr["mintReferral"],
            ),
            (
                curr["creatorReward"],
                curr["createReferralReward"],
                curr["firstMinterReward"],
                curr["mintReferralReward"],
            ),
        )

        total_zora_fees += curr["zoraReward"]  # Assuming curr.zoraReward is an integer

        for recipient, fee in recipients_and_fees:
            grouped_data[recipient][curr["rewardType"]] += fee
            grouped_data[recipient]["totalCreatorReward"] += fee
            total_creator_fees += fee
    return grouped_data, total_zora_fees, total_creator_fees


def generate_leaderboard_data(grouped_data: dict, chains: list):
    leaderboard_data = []
    for creator, rewards in grouped_data.items():
        leaderboard_entry = {
            "creator": creator,
            "totalCreatorReward": str(
                rewards["totalCreatorReward"]
            ),  # Convert to string
        }
        for chain in chains:
            leaderboard_entry[chain["key"]] = str(
                rewards[chain["key"]]
            )  # Add chain rewards
        leaderboard_data.append(leaderboard_entry)
    leaderboard_data.sort(
        key=lambda entry: int(entry["totalCreatorReward"]), reverse=True
    )
    return leaderboard_data
