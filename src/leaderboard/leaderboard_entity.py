from config import config
from sqlalchemy import Integer, String, TEXT, NUMERIC, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column


class Leaderboard(config.Base):
    __tablename__ = "RewardsDeposit_versioned"

    id: Mapped[str] = mapped_column(
        TEXT,
        primary_key=True,
        autoincrement=True,
        use_existing_column=True,
    )
    timestamp: Mapped[int] = mapped_column(
        NUMERIC(78),
        unique=True,
        use_existing_column=True,
    )
    chain: Mapped[str] = mapped_column(
        TEXT,
        use_existing_column=True,
    )
    sender: Mapped[str] = mapped_column(
        TEXT,
        name="from",
        use_existing_column=True,
    )
    createReferral: Mapped[str] = mapped_column(
        TEXT,
        name="createReferral",
        use_existing_column=True,
    )
    creator: Mapped[str] = mapped_column(
        TEXT,
        name="creator",
        use_existing_column=True,
    )
    mintReferral: Mapped[str] = mapped_column(
        TEXT,
        name="mintReferral",
        use_existing_column=True,
    )
    firstMinter: Mapped[str] = mapped_column(
        TEXT,
        name="firstMinter",
        use_existing_column=True,
    )
    zora: Mapped[str] = mapped_column(
        TEXT,
        name="zora",
        use_existing_column=True,
    )
    creatorReward: Mapped[int] = mapped_column(
        NUMERIC(78),
        name="creatorReward",
        use_existing_column=True,
    )
    createReferralReward: Mapped[int] = mapped_column(
        NUMERIC(78),
        name="createReferralReward",
        use_existing_column=True,
    )
    mintReferralReward: Mapped[int] = mapped_column(
        NUMERIC(78),
        name="mintReferralReward",
        use_existing_column=True,
    )
    firstMinterReward: Mapped[int] = mapped_column(
        NUMERIC(78),
        name="firstMinterReward",
        use_existing_column=True,
    )
    zoraReward: Mapped[int] = mapped_column(
        NUMERIC(78),
        name="zoraReward",
        use_existing_column=True,
    )
    effectiveFromCheckpoint: Mapped[str] = mapped_column(
        VARCHAR(58),
        name="effectiveFromCheckpoint",
        use_existing_column=True,
    )
    effectiveToCheckpoint: Mapped[str] = mapped_column(
        VARCHAR(58),
        name="effectiveToCheckpoint",
        use_existing_column=True,
    )
    __table_args__ = {"schema": "ponder_1707091779542"}
