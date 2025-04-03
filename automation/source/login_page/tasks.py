from playwright.sync_api import expect
from allure import step

from source.base_page.tasks import TasksBasePage
from config.data import Credentials


class TasksLoginPage(TasksBasePage):

    def auth(self, login: str = Credentials.username, password: str = Credentials.password) -> None:
        # Заполняем поле "Username"
        self.page.locator(text='Username').fill(value=login)
        self.report.attach_screenshot(self.page, name='Ввод логина')
        # Заполняем поле "Password"
        self.page.get_by_placeholder(text='Password').fill(value=password)
        self.report.attach_screenshot(self.page, name='Ввод пароля')
        # Нажимаем кнопку "Login"
        with step('Проверка конки войти'):
            expect(self.page.locator(selector='[data-test="login-button"]')).to_be_visible()
            self.report.attach_screenshot(self.page)
        self.page.locator(selector='[data-test="login-button"]').click()
