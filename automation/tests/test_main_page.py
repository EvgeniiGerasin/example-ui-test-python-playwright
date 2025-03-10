import allure
import pytest
from playwright.sync_api import Page, expect

from source.login_page.tasks import TasksLoginPage


class TestMainPage:

    @pytest.mark.parametrize(
        'locator',
        [
            "[data-test=\"inventory-list\"]",
            "[data-test=\"product-sort-container\"]",
            "[data-test=\"shopping-cart-link\"]",
            "[data-test=\"add-to-cart-sauce-labs-backpack\"]"
        ]
    )
    def test_open_page(self, page_fixture: Page, locator: str) -> None:
        with allure.step('Входим в систему'):
            login_page = TasksLoginPage(page=page_fixture)
            login_page.auth()
        with allure.step('Проверка окна с продуктами'):
            screenshot_bytes = page_fixture.screenshot()
            allure.attach(body=screenshot_bytes, name='sss', attachment_type=allure.attachment_type.PNG)
            expect(page_fixture.locator(locator)).to_be_visible()
