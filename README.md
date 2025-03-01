# FastAPI приложение с аутентификацией и авторизацией через JWT токен

## Описание
Этот проект представляет собой API, разработанное на FastAPI, с поддержкой аутентификации через JWT-токены и минимальной авторизацией и разлогиниванием

## Возможности
- Асинхронная работа с базой данных
- Регистрация пользователей с хешированием паролей
- Аутентификация через JWT
- Авторизация и разлогинивание
- Сохранение и удаление токена в coockies для автоматической авторизации & разлогинивания

## Установка и запуск
### 1. Установка зависимостей
Проект использует Poetry для управления зависимостями
```sh
poetry install
```
### 2. Настройка окружения
Создайте файл `.env` в корне проекта и добавьте в него нужные параметры:
```ini
APP_NAME=FastAPI_app
DOCKER=True
DB_USER=admin
DB_PASSWORD=password
DB_HOST_DOCKER=postgres
DB_HOST_LOCAL=localhost
DB_PORT=5432
DB_NAME=dbname

POSTGRES_USER=admin
POSTGRES_PASSWORD=password
POSTGRES_DB=dbname
PGDATA=/var/lib/postgresql/data/pgdata

SECRET_KEY=YOUR_SECRET_KEY
ALGORITHM=HS256
```

_Для запуска через Docker установите параметр True.  
Для запуска в командной строке - False._
```ini
DOCKER=True
```

### 3. Подключение к базе данных
В качестве СУБД в проекте используется PostgreSQL и Alembic для миграций базы данных.  
Перед первым запуском создайте миграции и примените их:
```sh
alembic revision --autogenerate -m "User and Post models"
alembic upgrade head
```

### 4. Запуск приложения
#### Через командную строку:
```sh
uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

#### Через Docker и docker-compose:

```sh
docker build -t fastapi_app .
docker-compose up -d
```

### 5. Документация API

После запуска API будет доступна документация Swagger по адресу:

```
http://localhost:8001/docs #при запуске через IDE
http://localhost:8000/docs #при запуске через Docker
```

## Принцип работы приложения

### 1) Получение списка пользователей
**Метод:** `GET /users/`

**Ответ:** JSON-массив объектов `User`
```json
[
  {
    "username": "string",
    "email": "user@example.com",
    "first_name": "string",
    "last_name": "string",
    "password": "string"
  }
]
```

### 2) Регистрация пользователя
**Метод:** `POST /users/register`

**Пример запроса:**
```json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}
```

**Пример ответа:**
```json
{"message": "Registration successful"}
```

### 3) Авторизация пользователя
**Метод:** `POST /users/login`

**Пример запроса:**
```json
{
  "email": "user@example.com",
  "password": "string"
}
```

**Пример ответа:**
```json
{
  "access_token": "token",
  "refresh_token": null
}
```

### 4) Получение данных профиля
**Метод:** `GET /users/me`

**Пример ответа:**
```json
{
  "username": "string",
  "email": "user@example.com",
  "first_name": "string",
  "last_name": "string",
  "password": "string"
}
```

### 5) Выход из системы
**Метод:** `POST /users/logout`

**Пример ответа:**
```json
{"message": "Logout successful"}
```


