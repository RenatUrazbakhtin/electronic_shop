# electronic_shop

## Описание проекта
Онлайн платформа торговой сети электроники

Сеть представляет собой структуру или 3 уровней:
- Завод(factory)
- Розничная сеть(net)
- Индивидуальный предприниматель(entrepreneur)

Каждое звено сети ссылается только на одного поставщика оборудования

В рамках проекта реализованна backend часть веб приложения с API интерфейсом и админ-панелью

## Технологии
- Python
- Pip
- Django
- DRF
- PostgreSQL
- Docker
- Docker-compose

## Зависимости
Зависимости проекта находятся в файле requirements

Установить зависимости можно с помощью команды pip install -r requirements

## env_sample
POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST(db) - данные для подключения к бд

SECRET_KEY - ключ django

## Работа с проектом
Для запуска проекта необходимо выполнить следующие шаги:
1) Установить на компьютер Docker и Docker Compose с помощью инструкции [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
2) Клонировать репозиторий себе на компьютер
3) Создать файл .env.prod по примеру .env_sample
4) Собрать Docker образ с помощью команды `docker-compose build`
5) Запустить контейнер с помощью команды `docker-compose up`
6) Сервер будет автоматически запущен по адрессу `127.0.0.1:8000`

## Тесты
Проект покрыт тестами на 90%

Проверить тесты коммандой `coverage run --source='.' manage.py test`
Узнать процент покрытия `coverage report`

При проверке тестов необходимо закомментировать значение `HOST` в settings.py блок DATABASES.

## Документация по ссылкам
Swagger - `swagger/`

Redoc - `redoc/`
