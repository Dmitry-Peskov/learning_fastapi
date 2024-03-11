from fastapi import FastAPI
from contextlib import asynccontextmanager
import uvicorn
from core.database import database
from core.models import BaseModel
from api_v1 import api_v1_router


@asynccontextmanager
async def launch_app(app: FastAPI):
    async with database.engine.begin() as connection:
        await connection.run_sync(BaseModel.metadata.create_all)
    yield


app = FastAPI(lifespan=launch_app)
app.include_router(api_v1_router)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
