import pytest

from pages.MainPage import MainPage
from config import LOGIN, PASSWORD, INCORRECT_PASSWORD
from playwright.sync_api import Page, expect


@pytest.mark.smoke
def test_login(main_page: MainPage):
    main_page.login(LOGIN,PASSWORD)
    expect(main_page.page).to_have_url('https://www.litres.ru/')

@pytest.mark.smoke
def test_login_success(authenticated_page):
    authenticated_page.goto('https://www.litres.ru/me/profile/')
    authenticated_page.wait_for_load_state('domcontentloaded')
    authenticated_page.get_by_text('Alex Apanyuk').wait_for(timeout=10000)
    assert authenticated_page.get_by_text('Alex Apanyuk').is_visible()

@pytest.mark.smoke
def test_unsuccess_auth(main_page: MainPage):
    main_page.login(LOGIN,INCORRECT_PASSWORD)
    expect(main_page.page.get_by_text("Неверное сочетание логина и пароля")).to_be_visible()

@pytest.mark.smoke
def test_order_history_is_empty(authenticated_page):
    authenticated_page.wait_for_load_state('load')
    authenticated_page.goto('https://www.litres.ru/me/profile/')
    authenticated_page.get_by_test_id('profile__menuItem--orders').click()
    expect(authenticated_page.get_by_text('Нет заказов')).to_be_visible()





