# Отчёт по отладке приложения Selectel Vacancies API

![alt text](image.png)

**ФИО:** Самохвалов А.С.  
**Дата:** 10 марта 2026

---

## Шаг 0: Анализ репы

- **Что сделал:** Изучил структуру проекта, `README.md`, `app/core/config.py` для определения переменных окружения.
- **Проблема:** Отсутствует `.env.example`. Переменные окружения описаны в README.md, но их значения нужно найти в коде.
- **Решение:** 
    1. Создал файл `.env` с переменными:
        - `DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/postgres`
        - `LOG_LEVEL=DEBUG`
        - `PARSE_SCHEDULE_MINUTES=5`
    2. Почистил `.gitignore` от избыточных строк (шаблон GitHub), оставил минимальный набор для Python-приложения.

---

## Шаг 1: Исправление бага №1 (Requirements)

- **Что сделал:** Перед запуском приложения проверил зависимости в `requirements.txt`.
- **Проблема:** Дублирующая строка со странной версией FastAPI.
- **Файл и строка:** `requirements.txt`
- **Решение:** Удалил строку `fastapi==999.0.0; python_version < "3.8"`
- **Причина ошибки:** Вероятно, добавленная несуществующая версия пакета (999.0.0) для старой версии python.
- **Итог:**
    1. Создал и активировал `venv`
    2. Установил зависимости из `requirements.txt`

---

## Шаг 2: Исправление бага №2 (Pydantic Config)

- **Что сделал:** Запустил Docker, получил ошибку валидации pydantic.
- **Проблема:** Контейнер падает с ошибкой `pydantic_core._pydantic_core.ValidationError: Extra inputs are not permitted`.
- **Файл и строка:** `app/core/config.py:10-18`
- **Код до исправления:**
    ```python
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    database_url: str = Field(
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres_typo",
        validation_alias="DATABSE_URL",
    )
    ```
- **Код после исправления:**
    ```python
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",  # FIX: Игнорируем системные переменные
    )

    database_url: str = Field(
        "postgresql+asyncpg://postgres:postgres@db:5432/postgres", # FIX: Исправлено имя БД по умолчанию
        validation_alias="DATABASE_URL", # FIX: Исправлена опечатка в алиасе
    )
    ```
- **Причина ошибки:** 
    1. Опечатка `validation_alias="DATABSE_URL"`.
    2. Значение строки подключения по умолчанию содержало некорректное имя БД (postgres_typo).
- **Итог:** Исправил опечатку в алиасе, теперь переменная из `.env` читается корректно.

---

## Шаг 3: Исправление бага №3 (Parser AttributeError)

- **Описание проблемы:** Фоновый парсинг падает с ошибкой `AttributeError: 'NoneType' object has no attribute 'name'`.
- **Файл и строка:** `app/services/parser.py:43`
- **Код до исправления:**
    ```python
    "city_name": item.city.name.strip(),
    ```
- **Код после исправления:**
    ```python
    "city_name": item.city.name.strip() if item.city else None,
    ```
- **Причина ошибки:** Попытка обращения к атрибуту `.name` у объекта типа `None`. Поле `city` является опциональным.
- **Итог:** Парсинг работает корректно, вакансии без города сохраняются с `city_name=None`.

---

## Шаг 4: Исправление бага №4 (scheduler)

- **Описание проблемы:** Фоновый парсинг запускается каждые 5 секунд вместо 5 минут
- **Файл и строка:** `app/services/scheduler.py` ?
- **Код до исправления:**
    ```python
    seconds=settings.parse_schedule_minutes,
    ```
- **Код после исправления:**
    ```python
    minutes=settings.parse_schedule_minutes,
    ```
- **Причина ошибки:** Использование именованного аргумента `seconds` вместо `minutes` в методе `add_job`.
- **Итог:** Интервал парсинга теперь соответствует настройкам (5 минут).

---

## Шаг 5: Исправление бага №5 ()
- **Описание проблемы:**
- **Файл и строка:**
- **Код до исправления:**
    ```python

    ```
- **Код после исправления:**
    ```python

    ```
- **Причина ошибки:** 
- **Итог:** 

#### Итог на текущий момент
* Контейнеры успешно запускаются и связываются друг с другом.
* База данных инициализируется, миграции Alembic проходят успешно.
* Фоновый парсер начал отправлять запросы к API Selectel (получен статус 200 OK).
* Перезапуск контейнера `docker compose down && docker compose up --build`

#### Планируемые шаги
- [x] Исправить интервал планировщика (сейчас срабатывает каждые 5 секунд вместо 5 минут).
- [ ] Протестировать CRUD эндпоинты через Swagger UI.
- [ ] `app/db/base.py` — пустой файл (только базовый класс)
- [ ] `app/api/v1/vacancies.py` - дублирование функции `get_session()` (в `vacancies.py` и `parse.py`).
- [ ] `app/crud/vacancy.py` — `upsert_external_vacancies` - функция считает только newly created, но не обновлённые
- [ ] `app/api/v1/vacancies.py` — POST возвращает 200 для дубликата (Обычно 409 Conflict или 400 Bad Request)
- [ ] `app/schemas/vacancy.py` — `VacancyUpdate` требует все поля (Обычно для update - Optional, обновлять частично.)
- [ ] `app/crud/vacancy.py` — фильтр по городу использует `city_name`. Параметр `city` из запроса не будет передан в `list_vacancies`, потому что имена не совпадают.
- [ ] Выявить и исправить остальные баги (3/8)
