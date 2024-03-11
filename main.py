from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from core.database import database
from core.models import BaseModel


@asynccontextmanager
async def launch_app(app: FastAPI):
    async with database.engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=launch_app)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
