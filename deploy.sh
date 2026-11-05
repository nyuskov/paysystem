#!/bin/bash

# Функция, которая сработает при нажатии Ctrl+C
cleanup() {
    echo ""
    echo "🛑 Перехвачен сигнал остановки (Ctrl+C)..."
    echo "🗑️ Останавливаем контейнеры проекта..."
    # Без -v: named volumes (node_modules, pnpm-store) сохраняем,
    # иначе при каждом запуске зависимости ставятся заново
    docker compose down
    echo "✅ Все контейнеры успешно остановлены и удалены."
    exit 0
}

# Регистрируем перехват Ctrl+C (сигнал SIGINT) и привязываем к функции cleanup
trap cleanup SIGINT

echo "🚀 Запуск FastAPI в LIVE-режиме разработки..."

# container_name в compose глобальны: если остался контейнер от прошлого запуска
# или из другой папки, docker compose упадёт с "name is already in use".
# Убираем такие остатки заранее (для dev это безопасно).
docker rm -f fastapi_app nuxt_frontend traefik >/dev/null 2>&1 || true

# 1. Собираем и поднимаем контейнеры в фоне
docker compose up -d --build --force-recreate --remove-orphans

echo ""
echo "🖥️ Подключаемся к логам FastAPI в реальном времени..."
echo "💡 Редактируйте код на ПК — сервер внутри Docker будет перезапускаться сам."
echo "🛑 Для полной остановки проекта и удаления контейнеров нажмите Ctrl+C."
echo "----------------------------------------------------------------------------------------"

# 2. Выводим логи. Скрипт будет «висеть» на этой строке, пока вы не нажмете Ctrl+C
docker compose logs -f backend frontend
