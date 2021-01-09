# Телеграм-Бот постинга матчей CS:GO из HLTV
## Фичи
* Фильтр стран
* Отправка в телеграм

## Установка 
* Создать и заполнить .env из .env.example
* Выполнить `alembic upgrade head`
* Получить json ключ и установить его по этой инструскции https://stackoverflow.com/questions/56875958/how-to-authenticate-docker-container-with-google-service
## Миграции
Создание

`alembic revision --autogenerate -m "Migration name"`

Применение 

`alembic upgrade head`
