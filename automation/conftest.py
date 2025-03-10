from playwright.sync_api import sync_playwright, Browser, Page
import pytest
from config.data import Stands


@pytest.fixture(scope="function")
def page_fixture():
    # Запускаем Playwright в синхронном режиме
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser: Browser = playwright.chromium.launch(headless=True)
        # Создаем новую страницу
        page: Page = browser.new_page()
        # Переходим на указанный URL
        page.goto(url=Stands.url)
        # Передаем страницу в тест
        yield page
        # Закрываем страницу и браузер после завершения теста
        page.close()
        browser.close()
