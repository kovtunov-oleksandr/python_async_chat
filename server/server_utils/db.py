import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from server.config import engine
from server.models.user import User, Base

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def recreate_db_force():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def create_user(nickname: str, password: str, email: str = None):
    async with async_session() as conn:
        async with conn.begin():
            user = User(nickname=f'{nickname}', password=f'{password}', email=f'{email}')
            conn.add(user)


async def select_data_from_table(tablename: Base):
    async with async_session() as session:
        result = await session.execute(select(tablename))
        data_list = [row for row in result.scalars().fetchall()]
        return data_list


async def main():
    await asyncio.create_task(recreate_db_force())
    await asyncio.create_task(create_user('Nick_1', 'pass2134', '2sda92@gmail.com'))
    await asyncio.create_task(create_user('Nick_2', 'pass12334', 'lasds102@gmail.com'))
    await asyncio.create_task(create_user('Nick_3', 'pass12rew', 'asd1qs02@gmail.com'))
    await asyncio.create_task(create_user('Nick_4', 'pass11234', 'l1202@gmail.com'))


if __name__ == '__main__':
    asyncio.run(main())
