import pytest
from pages.MainPage import MainPage
from pages.ProfilePage import ProfilePage
from playwright.sync_api import Page, Browser, Playwright
from config import LOGIN, PASSWORD


@pytest.fixture
def main_page(page: Page):
    return MainPage(page)

@pytest.fixture
def profile_page(page: Page):
    return ProfilePage(page)

@pytest.fixture(autouse=True)
def open_main_page(page: Page):
    page.goto('https://www.litres.ru/')
    yield


@pytest.fixture(scope='module')
def browser_module(playwright: Playwright):
    browser = playwright.chromium.launch()
    yield browser
    browser.close()

@pytest.fixture(scope='module')
def authenticated_page(browser_module):
    print("=== browser launched ===")
    context = browser_module.new_context()
    page = context.new_page()
    print("=== page created ===")

    main_page = MainPage(page)
    main_page.login(LOGIN, PASSWORD)
    main_page.page.wait_for_url('https://www.litres.ru/')  # ждём что залогинились
    page.wait_for_load_state('load')
    print("=== login done ===")
    print("=== page loaded ===")

    yield page

    context.close()

