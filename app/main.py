from fastapi import FastAPI, APIRouter
import httpx
from fastapi import APIRouter, HTTPException

app = FastAPI(openapi_url="/api/v1/billiards/openapi.json", docs_url="/api/v1/billiards/docs")

billiards_router = APIRouter()

billiards = [
    {
        'billiards_id': 1,
        'name': 'Клуб "Бильярдный Рай"',
        'description': 'Клуб "Бильярдный Рай" - это современный бильярдный клуб в самом сердце Москвы, предлагающий высококачественные столы и оборудование для игроков всех уровней.',
        'address': 'ул. Проходчиков, д. 123',
        'country': 'Россия'
    },
    {
        'billiards_id': 2,
        'name': 'Бильярдный Гений',
        'description': 'Бильярдный Гений славится своими уютными интерьерами и качественными бильярдными столами, привлекая ценителей бильярда со всей Москвы.',
        'address': 'пр-т. Шарова, д. 456',
        'country': 'Россия'
    },
    {
        'billiards_id': 3,
        'name': 'Центр Бильярда "Мастер"',
        'description': 'Центр Бильярда "Мастер" проводит регулярные турниры и предлагает программы обучения для начинающих игроков, содействуя развитию живого бильярдного сообщества в Москве.',
        'address': 'ул. Кийковая, д. 789',
        'country': 'Россия'
    },
    {
        'billiards_id': 4,
        'name': 'Алмазный Кий',
        'description': 'Бильярдный клуб "Алмазный Кий" известен своими аккуратно поддерживаемыми столами и дружественной атмосферой, что делает его любимым местом для бильярдных афиционадо в Москве.',
        'address': 'пр-т. Ямского Поля, д. 321',
        'country': 'Россия'
    },
    {
        'billiards_id': 5,
        'name': 'Мастера Бильярда Москвы',
        'description': 'Клуб "Мастера Бильярда Москвы" предлагает современные бильярдные залы, оборудованные последними технологиями, привлекая как случайных игроков, так и серьезных соперников.',
        'address': 'пр-т. Мастеров, д. 987',
        'country': 'Россия'
    }
]


@billiards_router.get("/")
async def read_billiards():
    return billiards


@billiards_router.get("/{billiards_id}")
async def read_companie(billiards_id: int):
    for companie in billiards:
        if companie['billiards_id'] == billiards_id:
            return companie
    return None


app.include_router(billiards_router, prefix='/api/v1/billiards', tags=['billiards'])

if __name__ == '__main__':
    import uvicorn
    import os

    try:
        PORT = int(os.environ['PORT'])
    except KeyError as keyerr:
        PORT = 80
    uvicorn.run(app, host='0.0.0.0', port=PORT)
