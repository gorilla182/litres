from playwright.sync_api import Page
from pages.BasePage import BasePage


class MainPage(BasePage):
    BASE_URL='https://www.litres.ru/'
    MAIN_PAGE_SIGN_IN_BUTTON='header__login-button--desktop'
    LOGIN_PLACEHOLDER='auth__input--enterEmailOrLogin'
    LOGIN_PAGE_CONTINUE_BUTTON='auth__button--continue'
    PASSWORD_PLACEHOLDER='auth__input--enterPassword'
    PASSWORD_PAGE_AUTH_BUTTON='auth__button--enter'
    PROFILE_URL='https://www.litres.ru/me/profile/'

    def __init__(self, page: Page): #переопределяем метод родителя
        super().__init__(page) #вызываем конструктор родителя, чтобы пользоваться его методами

        self.login_button = page.get_by_test_id(self.MAIN_PAGE_SIGN_IN_BUTTON)
        self.login_placeholder = page.get_by_test_id(self.LOGIN_PLACEHOLDER)
        self.continue_after_fill=page.get_by_test_id(self.LOGIN_PAGE_CONTINUE_BUTTON)
        self.password_fill=page.get_by_test_id(self.PASSWORD_PLACEHOLDER)
        self.continue_after_password_fill=page.get_by_test_id(self.PASSWORD_PAGE_AUTH_BUTTON)

    def login(self, login, password):
        self.page.goto(self.BASE_URL)
        self.login_button.click()
        self.login_placeholder.fill(login)
        self.continue_after_fill.click()
        self.password_fill.fill(password)
        self.continue_after_password_fill.click()
        self.page.wait_for_url('https://www.litres.ru/')  # ждём что залогинились
        self.page.wait_for_load_state('load')


    def go_to_profile(self, page: Page):
        page.goto(self.PROFILE_URL)


