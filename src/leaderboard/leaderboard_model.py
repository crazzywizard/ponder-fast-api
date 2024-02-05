from pydantic import BaseModel


class Leaderboard(BaseModel):
    name: str


class LeaderboardData(BaseModel):
    creator: str
    totalCreatorReward: str
    mainnetReward: str
    optimismReward: str
    baseReward: str
    zoraReward: str


class LeaderboardResponse(BaseModel):
    leaderboard_data: list[LeaderboardData]
    recordsCount: int
    totalZoraFees: str
    totalCreatorFees: str


class LeaderboardRawResponse(BaseModel):
    createReferral: str
    timestamp: int
    sender: str
    mintReferral: str
    zora: str
    createReferralReward: int
    firstMinterReward: int
    effectiveFromCheckpoint: str
    id: str
    chain: str
    creator: str
    firstMinter: str
    creatorReward: int
    mintReferralReward: int
    zoraReward: int
    effectiveToCheckpoint: str
