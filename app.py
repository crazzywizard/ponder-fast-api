from config import config
from nest.core.app import App
from src.leaderboard.leaderboard_module import LeaderboardModule
from fastapi.middleware.cors import CORSMiddleware

app = App(description="Indexer Service", modules=[LeaderboardModule])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await config.create_all()
    print("App started")
