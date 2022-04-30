# настройка окружения, проходит один раз, кроме 2ого пункта

1. python -m venv venv
2. .\venv\scripts\activate.ps1
3. pip install -r requirements.txt

# запуск автотестов

pytest test_wildberries.py


# подтягивание изменений

1. git fetch
2. git pull origin main
