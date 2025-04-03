from playwright.sync_api import Page

from tools.reporter import AllureReporter


class TasksBasePage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self.report = AllureReporter()
