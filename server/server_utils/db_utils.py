from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from server.config import engine
from server.models.user import Base

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def recreate_db_force():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
