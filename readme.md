# Телеграм-Бот постинга матчей CS:GO из HLTV
## Фичи
* Фильтр стран
* Отправка в телеграм

## Установка 
* Создать и заполнить .env из .env.example
* Выполнить `alembic upgrade head`
## Миграции
Создание

`alembic revision --autogenerate -m "Migration name"`

Применение 

`alembic upgrade head`
