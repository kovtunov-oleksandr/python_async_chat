import asyncio

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker

from arhiv.PycharmProjects.pythonProject.homework.artur_yastrebov.sqlalchemy_asyncio.server.config import engine
from arhiv.PycharmProjects.pythonProject.homework.artur_yastrebov.sqlalchemy_asyncio.server.models.user import User, \
    Base

async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)

# async def async_select():
    # async with async_session() as conn:
    #     result = await conn.execute('SELECT * FROM Users')
    #     for row in result:
    #         print(row)

async def async_clear_all():

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def async_add(nickname,password,email = None):

    async with async_session() as conn:
        async with conn.begin():
            user = User(nickname=f'{nickname}', password=f'{password}', email=f'{email}')
            conn.add(user)

async def async_select():
    async with async_session() as session:
        result = await session.execute(select(User))

        for row in result.scalars().fetchall():
            await session.commit()
            print(row.nickname, row.password, row.email)


asyncio.run(async_clear_all())
asyncio.run(async_add('Nick_1', 'pass2134', '2sda92@gmail.com'))
asyncio.run(async_add('Nick_2', 'pass12334', 'lasds102@gmail.com'))
asyncio.run(async_add('Nick_3', 'pass12rew', 'asd1qs02@gmail.com'))
asyncio.run(async_add('Nick_4', 'pass11234', 'l1202@gmail.com'))
asyncio.run(async_select())

