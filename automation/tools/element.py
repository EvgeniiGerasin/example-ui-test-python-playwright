from playwright.sync_api import Page
from playwright.sync_api._generated import Locator
from tools.reporter import AllureReporter


class WebElement:

    def __init__(self, page: Page):
        self.page: Page = page

    # def click(self):
    #     with AllureReporter.step(f"Click on '{self.name}'"):
    #         self.page.locator(self.xpath).click()
    #         AllureReporter.log_action(self.name, "clicked")
    #         AllureReporter.attach_screenshot(self.page, f"After clicking {self.name}")

    # def fill(self, text: str):
    #     with AllureReporter.step(f"Fill '{self.name}' with '{text}'"):
    #         self.page.locator(self.xpath).fill(text)
    #         AllureReporter.log_action(self.name, "filled", text)
    #         AllureReporter.attach_screenshot(self.page, f"After filling {self.name}")

    # def get_text(self) -> str:
    #     with AllureReporter.step(f"Get text from '{self.name}'"):
    #         text = self.page.locator(self.xpath).text_content()
    #         AllureReporter.log_action(self.name, "text extracted", text)
    #         return text


    

    
