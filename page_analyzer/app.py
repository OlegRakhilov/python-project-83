"""Page Analyzer Application."""
import os
from typing import Any

from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for

from page_analyzer.checker import get_check_info
from page_analyzer.normalizer import normalize_url
from page_analyzer.repository import ChecksRepository, UrlsRepository
from page_analyzer.validator import validate

load_dotenv()
app = Flask(__name__)

app.config['DATABASE_URL'] = os.getenv('DATABASE_URL')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-123')

def get_repositories():
    db_url = app.config['DATABASE_URL']
    return UrlsRepository(db_url), ChecksRepository(db_url)

@app.route("/")

def index():
    """Render index page."""
    return render_template("index.html")


@app.route("/urls")
def urls():
    repo = UrlsRepository(app.config["DATABASE_URL"])
    urls_list = repo.get_url_with_checks()
    return render_template("urls.html", urls=urls_list)


@app.route("/urls", methods=["POST"])

def create_url():
    """Create new url entry."""
    repo = UrlsRepository(app.config["DATABASE_URL"])
    checks_repo = ChecksRepository(app.config["DATABASE_URL"])

    errors = validate(url)
    for error in errors.values():
        flash(error, "error")
        return render_template("index.html", url=url, errors=errors), 422  # noqa: E501

    normalized_url = normalize_url(url)

    existing_url = repo.find_by_name(normalized_url)
    if existing_url:
        flash("Страница уже существует", "error")
        return redirect(url_for("show_urls_info", url_id=existing_url["id"]))

    saved_id = repo.save(normalized_url)

    flash("Страница успешно добавлена", "success")
    return redirect(url_for("show_urls_info", url_id=saved_id))


@app.route("/urls/<int:url_id>")
def show_urls_info(url_id: int) -> str:
    """Show specific url details."""
    # Получаем URL базы из конфига
    db_url = app.config.get("DATABASE_URL")
    # Создаем репозитории прямо здесь
    repo = UrlsRepository(app.config["DATABASE_URL"])
    checks_repo = ChecksRepository(app.config["DATABASE_URL"])

    url = repo.find(url_id)
    if not url:
        flash("Страница не найдена", "error")
        return redirect(url_for("urls"))

    checks = checks_repo.get_checks_by_url_id(url_id)
    return render_template("url_info.html", url=url, checks=checks)

@app.route("/urls/<int:url_id>/checks", methods=["POST"])
def check_url(url_id: int) -> Any:
    """Run check for a specific url."""
    # ДОБАВЬТЕ ЭТИ СТРОКИ:
    db_url = app.config.get("DATABASE_URL")
    repo = UrlsRepository(app.config["DATABASE_URL"])
    checks_repo = ChecksRepository(app.config["DATABASE_URL"])

    # Теперь код ниже будет работать:
    url = repo.find(url_id)
    if not url:
        flash("Страница не найдена", "error")
        return redirect(url_for("urls"))

    check_data = get_check_info(url["name"])

    if check_data and checks_repo.create_check(url_id, check_data):
        flash("Страница успешно проверена", "success")
    else:
        flash("Произошла ошибка при проверке", "error")

    return redirect(url_for("show_urls_info", url_id=url_id))


if __name__ == "__main__":
    app.run(debug=True)
