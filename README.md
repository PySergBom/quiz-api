## О проекте

Этот проект предназначен для автоматизации получения англоязычных вопросов для викторины и их хранения в базе данных PostgreSQL.
Он облегчает развертывание необходимых компонентов, предоставляет простой способ взаимодействия с API викторин,
и обеспечивает устойчивое сохранение данных при перезапуске.

## Стек

<img alt="Python" src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/>	<img src="https://img.shields.io/badge/fastapi%20-%2313988a.svg?&style=for-the-badge&logo=data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiIHN0YW5kYWxvbmU9Im5vIj8+CjxzdmcKICAgeG1sbnM6ZGM9Imh0dHA6Ly9wdXJsLm9yZy9kYy9lbGVtZW50cy8xLjEvIgogICB4bWxuczpjYz0iaHR0cDovL2NyZWF0aXZlY29tbW9ucy5vcmcvbnMjIgogICB4bWxuczpyZGY9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkvMDIvMjItcmRmLXN5bnRheC1ucyMiCiAgIHhtbG5zOnN2Zz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciCiAgIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIKICAgaWQ9InN2ZzgiCiAgIHZlcnNpb249IjEuMSIKICAgdmlld0JveD0iMCAwIDYuMzQ5OTk5OSA2LjM0OTk5OTkiCiAgIGhlaWdodD0iNi4zNDk5OTk5bW0iCiAgIHdpZHRoPSI2LjM0OTk5OTltbSI+CiAgPGRlZnMKICAgICBpZD0iZGVmczIiIC8+CiAgPG1ldGFkYXRhCiAgICAgaWQ9Im1ldGFkYXRhNSI+CiAgICA8cmRmOlJERj4KICAgICAgPGNjOldvcmsKICAgICAgICAgcmRmOmFib3V0PSIiPgogICAgICAgIDxkYzpmb3JtYXQ+aW1hZ2Uvc3ZnK3htbDwvZGM6Zm9ybWF0PgogICAgICAgIDxkYzp0eXBlCiAgICAgICAgICAgcmRmOnJlc291cmNlPSJodHRwOi8vcHVybC5vcmcvZGMvZGNtaXR5cGUvU3RpbGxJbWFnZSIgLz4KICAgICAgICA8ZGM6dGl0bGU+PC9kYzp0aXRsZT4KICAgICAgPC9jYzpXb3JrPgogICAgPC9yZGY6UkRGPgogIDwvbWV0YWRhdGE+CiAgPGcKICAgICB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtODcuNTM5Mjg2LC04NC40MjYxOTEpIgogICAgIGlkPSJsYXllcjEiPgogICAgPHBhdGgKICAgICAgIGlkPSJwYXRoODE1IgogICAgICAgZD0ibSA4Ny41MzkyODYsODQuNDI2MTkxIGggNi4zNSB2IDYuMzUgaCAtNi4zNSB6IgogICAgICAgc3R5bGU9ImZpbGw6bm9uZTtzdHJva2Utd2lkdGg6MC4yNjQ1ODMzMiIgLz4KICAgIDxwYXRoCiAgICAgICBzdHlsZT0ic3Ryb2tlLXdpZHRoOjAuMjY0NTgzMzI7ZmlsbDojZmZmZmZmIgogICAgICAgaWQ9InBhdGg4MTciCiAgICAgICBkPSJtIDkwLjcxNDI4Niw4NC45NjA2NDkgYyAtMS40NTc4NTQsMCAtMi42NDA1NDIsMS4xODI2ODggLTIuNjQwNTQyLDIuNjQwNTQyIDAsMS40NTc4NTQgMS4xODI2ODgsMi42NDA1NDIgMi42NDA1NDIsMi42NDA1NDIgMS40NTc4NTQsMCAyLjY0MDU0MiwtMS4xODI2ODggMi42NDA1NDIsLTIuNjQwNTQyIDAsLTEuNDU3ODU0IC0xLjE4MjY4OCwtMi42NDA1NDIgLTIuNjQwNTQyLC0yLjY0MDU0MiB6IG0gLTAuMTM3NTgzLDQuNzU3MjA5IHYgLTEuNjU2MjkyIGggLTAuOTIwNzUgbCAxLjMyMjkxNiwtMi41NzcwNDIgdiAxLjY1NjI5MiBoIDAuODg2MzU0IHoiIC8+CiAgPC9nPgo8L3N2Zz4K"/>
<img alt="Postgres" src ="https://img.shields.io/badge/postgres-%23316192.svg?&style=for-the-badge&logo=postgresql&logoColor=white"/>	
<img src="https://img.shields.io/badge/docker%20-%230db7ed.svg?&style=for-the-badge&logo=docker&logoColor=white"/>

**Компоненты:**

1. Docker-Compose с **PostgreSQL**:<br>
Проект включает файл docker-compose.yml, который позволяет легко развернуть контейнер с PostgreSQL и обеспечивает сохранность данных при перезапуске контейнера с использованием volumes на хост-машине.
Также для удобства в проект добавлен контейнер с **PGAdmin** для мониторинга БД.

2. Веб-сервис с использованием **FastAPI**:<br>
Реализован простой веб-сервис, предоставляющий REST API для обработки POST запросов с параметром questions_num в формате {"questions_num": integer}.
Веб-сервис способен взаимодействовать с публичным API (https://jservice.io/api/random?count=1) для получения англоязычных вопросов для викторины.
Полученные вопросы сохраняются в базе данных PostgreSQL, при этом проверяется уникальность вопросов.
Если вопрос уже существует в базе, производится повторный запрос к API до получения уникального вопроса.


## Установка и запуск
Клонируйте репозиторий и перейдите в рабочую директорию
```
git clone https://github.com/PySergBom/quiz-api.git
cd quiz-api
```
Запустите docker-compose:
```
docker-compose build
docker-compose up
```

## Документация
### Веб сервис
После запуска сервера документация доступна по адресу:
```
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```

<img src="https://github.com/PySergBom/quiz-api/assets/125088101/49de427f-be68-4dd7-a047-586b3a3e051c" width="400" />

Доступно 2 endpoint'а:<br>
1. questions для POST запросов. Для получения вопросов викторины отпубличного API и записи в БД
2. last_db_question для GET запросов. Возвращает последнюю запись БД

### pgAdmin

```
http://127.0.0.1:5050/
login: admin@admin
password: admin
```

## Пример POST-запроса:

URL: `http://127.0.0.1:8000/questions`

Request body: `{question_num: 10}`

Response: `"Question"`

![image](https://github.com/PySergBom/quiz-api/assets/125088101/0c264bb5-f7d8-4aa0-89d9-8986ed41ad18)

## Пример GET-запроса:

URL: `http://127.0.0.1:8000/last_db_question`
![image](https://github.com/PySergBom/quiz-api/assets/125088101/118c703f-7342-4876-a6b9-30b30dd63427)

