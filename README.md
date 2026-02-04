### Hexlet tests and linter status:
[![Actions Status](https://github.com/OlegRakhilov/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OlegRakhilov/python-project-83/actions)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OlegRakhilov_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OlegRakhilov_python-project-83)

Page Analyzer
### Описание
**Анализатор страниц** — это полноценное веб-приложение на Flask, которое позволяет анализировать указанные сайты на соответствие SEO-параметрам. Оно проверяет доступность сайта, извлекает теги H1, Title и описание (meta description).

Демо
Вы можете посмотреть, как работает приложение, по этой ссылке:
https://python-project-83-lr6q.onrender.com

Стек технологий
* **Python 3.13**
* **Flask** (веб-фреймворк)
* **PostgreSQL** (база данных)
* **Gunicorn** (WSGI-сервер)
* **BeautifulSoup4** (парсинг HTML)
* **uv** (пакетный менеджер)
* **Ruff** (линтер)

### Установка

1.  **Клонируйте репозиторий:**
    HTTPS: https://github.com
    SSH: git@github.com:OlegRakhilov/python-project-83.git
 2.  **Установите зависимости (используя uv):**
    ```bash
    make install
    ```

3.  **Настройте переменные окружения:**
    Создайте файл `.env` в корне проекта и добавьте:
    ```env
    DATABASE_URL=postgresql://username:password@localhost:5432/database_name
    SECRET_KEY=your_secret_key
    ```

4.  **Подготовьте базу данных:**
    ```bash
    psql -d database_name -f database.sql
    ```

### Запуск

**В режиме разработки:**
```bash
make dev  

Продакшн-версия (через Gunicorn):
bash
make start