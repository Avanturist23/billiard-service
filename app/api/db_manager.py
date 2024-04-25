from app.api.models import BilliardIn
from app.api.db import billiards, database


async def add_billiard(payload: BilliardIn):
    query = billiards.insert().values(**payload.dict())
    return await database.execute(query=query)


async def billiards():
    query = billiards.select()
    return await database.fetch_all(query=query)


async def get_billiard(id):
    query = billiards.select(billiards.c.id == id)
    return await database.fetch_one(query=query)


async def delete_billiard(id: int):
    query = billiards.delete().where(billiards.c.id == id)
    return await database.execute(query=query)


async def update_billiard(id: int, payload: BilliardIn):
    query = (
        billiards
        .update()
        .where(billiards.c.id == id)
        .values(**payload.dict())
    )
    return await database.execute(query=query)
