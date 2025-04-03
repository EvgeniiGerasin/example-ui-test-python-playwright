from playwright.sync_api import sync_playwright, Browser, Page
import pytest
from config.data import Stands


@pytest.fixture(scope="function")
def page_fixture():
    # Инициализация Playwright
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser: Browser = playwright.chromium.launch(headless=True)
        
        # Создаем контекст с поддержкой трассировки
        context = browser.new_context()

        # Начинаем запись трассировки
        context.tracing.start(name="trace", screenshots=True, snapshots=True)

        # Создаем новую страницу
        page: Page = context.new_page()

        # Переходим на указанный URL
        page.goto(url=Stands.url)

        # Передаем страницу в тест
        yield page

        # Останавливаем трассировку и сохраняем её в файл
        context.tracing.stop(path="trace.zip")

        # Закрываем страницу, контекст и браузер
        page.close()
        context.close()
        browser.close()