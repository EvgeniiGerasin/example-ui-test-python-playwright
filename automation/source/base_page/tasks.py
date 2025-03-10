from playwright.sync_api import Page


class TasksBasePage:

    def __init__(self, page: Page) -> None:
        self.page: Page = page
