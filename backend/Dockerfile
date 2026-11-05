# Используем стабильный образ Python 3.13
FROM python:3.13-slim

# Отключаем буферизацию логов и запись .pyc файлов
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Создаем чистое виртуальное окружение и сразу добавляем его в PATH,
# чтобы все последующие команды (включая запуск FastAPI) вызывали Python оттуда
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Устанавливаем Poetry прямо внутрь созданного виртуального окружения
RUN pip install --no-cache-dir poetry==2.0.1

# Копируем только файлы зависимостей
COPY pyproject.toml poetry.lock* /app/

# Синхронизируем пакеты (теперь они без конфликтов встанут в /opt/venv)
RUN poetry sync --only main --no-root --no-interaction --no-ansi

# Копируем весь остальной код проекта в /app
COPY . /app

# Запускаем FastAPI из виртуального окружения
CMD ["poetry", "run", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers", "--reload"]
