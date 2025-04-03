import allure
from datetime import datetime
from playwright.sync_api import Page


class AllureReporter:

    @staticmethod
    def step(step_name: str):
        """Декоратор для обертки действий в allure-шаги."""
        return allure.step(title=step_name)

    @staticmethod
    def attach_screenshot(page: Page, name: str = "Screenshot"):
        """Прикрепляет скриншот к отчету Allure."""
        screenshot: bytes = page.screenshot()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )

    @staticmethod
    def log_action(element_name: str, action: str, value: str = None):
        """Логирует действие с элементом."""
        message = f"🔹 {element_name}: {action}"
        if value:
            message += f" -> '{value}'"
        with allure.step(message):
            pass
