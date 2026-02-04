### Hexlet tests and linter status:
[![Actions Status](https://github.com/OlegRakhilov/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/OlegRakhilov/python-project-83/actions)

Page Analyzer
Page Analyzer is a Flask web application that allows users to analyze web pages for SEO effectiveness. The application checks the availability of websites and analyzes elements such as headers, descriptions, and H1 tags.

Features
URL availability check.
Analysis of title and description tags.
Display of check results on the user interface.
Demo
You can view the application in action at this link:
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

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=OlegRakhilov_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=OlegRakhilov_python-project-83)