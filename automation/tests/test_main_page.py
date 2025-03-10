import allure
from playwright.sync_api import Page, expect

from source.login_page.tasks import TasksLoginPage


class TestMainPage:

    def test_open_page(self, page_fixture: Page) -> None:
        with allure.step('Входим в систему'):
            login_page = TasksLoginPage(page=page_fixture)
            login_page.auth()
        with allure.step('Проверка окна с продуктами'):
            expect(page_fixture.locator("[data-test=\"title\"]")).to_contain_text("Products")
            screenshot_bytes = page_fixture.screenshot()
            allure.attach(body=screenshot_bytes, name='sss', attachment_type=allure.attachment_type.PNG)
            expect(page_fixture.locator("[data-test=\"inventory-list\"]")).to_contain_text("$")
            expect(page_fixture.locator("[data-test=\"product-sort-container\"]")).to_be_visible()
            expect(page_fixture.locator("[data-test=\"shopping-cart-link\"]")).to_be_visible()
            expect(page_fixture.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")).to_be_visible()
            screenshot_bytes = page_fixture.screenshot()
            allure.attach(body=screenshot_bytes, name='sss', attachment_type=allure.attachment_type.PNG)
