from nest.core.database.orm_provider import AsyncOrmProvider
import os
from dotenv import load_dotenv

load_dotenv()

config = AsyncOrmProvider(
    db_type="postgresql",
    config_params=dict(
        host=os.getenv("POSTGRESQL_HOST", "db"),
        db_name=os.getenv("POSTGRES_DB", "default_nest_db"),
        user=os.getenv("POSTGRES_USER", "postgres"),
        password=os.getenv("POSTGRES_PASSWORD", "postgres"),
        port=int(os.getenv("POSTGRESQL_PORT", 5432)),
    ),
)
