
from source.base_page.tasks import TasksBasePage

from config.data import Credentials


class TasksLoginPage(TasksBasePage):

    def auth(self, login: str = Credentials.username, password: str = Credentials.password) -> None:
        # Заполняем поле "Username"
        self.page.get_by_placeholder(text='Username').fill(value=login)
        # Заполняем поле "Password"
        self.page.get_by_placeholder(text='Password').fill(value=password)
        # Нажимаем кнопку "Login"
        self.page.locator(selector='[data-test="login-button"]').click()
