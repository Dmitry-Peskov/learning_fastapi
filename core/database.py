from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from config import settings


class DataBase:

    def __init__(self):
        self.engine = create_async_engine(
            url=settings.db_dsn,
            echo=settings.db_echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )


database = DataBase()
