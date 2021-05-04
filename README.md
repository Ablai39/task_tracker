Сделал авторизацию на jwt RDF в приложении users.
В приложении trackApp успел написать немного моделей для таблиц.
Есть немного фронта.
БД на postgres.

1. Можно генерить пользователей через POST запросы, я использовал Postman
Пример: 
    http://192.168.1.6:8000/user/create/
{
    "email": "nsdsdew@gmail.com",
    "first_name": "Ablai",
    "last_name": "Orazaliyev",
    "password": "qweQsdsdWE1234"
}

Результат:
{
    "id": 9,
    "email": "nsdsdew@gmail.com",
    "first_name": "Ablai",
    "last_name": "Orazaliyev",
    "date_joined": "2021-04-15T15:00:19.711485Z"
}

2. Аутентификация пользователей
Пример: 
    http://192.168.1.6:8000/user/obtain_token/
{
    "email": "nsdsdew@gmail.com",
    "password": "qweQsdsdWE1234"
}

Результат:
{
    "name": "Almas Almasov",
    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Im5ld0BnbWFpbC5jb20iLCJleHAiOjE2MTg0OTY4NDcsImVtYWlsIjoibmV3QGdtYWlsLmNvbSJ9.rv8b7bKf1SZEXWHEPa4Gy-zKEn2OfO2H-u6v_iJlwqM"
}

3. GET запрос Получение и обновление пользователей
Ключи:
Authorization = Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Im5ld0BnbWFpbC5jb20iLCJleHAiOjE2MTg0OTY4NDcsImVtYWlsIjoibmV3QGdtYWlsLmNvbSJ9.rv8b7bKf1SZEXWHEPa4Gy-zKEn2OfO2H-u6v_iJlwqM
Пример: 
    http://192.168.1.6:8000/user/update/

Результат:
{
    "id": 9,
    "email": "nsdsdew@gmail.com",
    "first_name": "Ablai",
    "last_name": "Orazaliyev",
    "date_joined": "2021-04-15T15:00:19.711485Z"
}
