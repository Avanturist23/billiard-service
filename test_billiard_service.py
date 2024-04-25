import requests


def test_get_all_clubs(url: str):
    res = requests.get(url).json()
    assert (res == [{
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
    }])


def test_get_club_by_id(url: str):
    res = requests.get(url).json()
    assert (res == {
        'billiards_id': 1,
        'name': 'Клуб "Бильярдный Рай"',
        'description': 'Клуб "Бильярдный Рай" - это современный бильярдный клуб в самом сердце Москвы, предлагающий высококачественные столы и оборудование для игроков всех уровней.',
        'address': 'ул. Проходчиков, д. 123',
        'country': 'Россия'
    })


if __name__ == '__main__':
    URL = 'http://127.0.0.1:80/api/v1/clubs/'
    test_get_club_by_id(URL + '1')
    test_get_all_clubs(URL)