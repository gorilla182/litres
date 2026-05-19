from pages.BasePage import BasePage
from playwright.sync_api import Page


class ProfilePage(BasePage):
    BASE_URL='https://www.litres.ru/me/profile/'
    PROFILE_NAME_LOCATOR='profile__userNameMain'
    AVATAR_LOCATOR='profile__avatarMain'
    USER_ORDER_HISTORY_LOCATOR='profile__menuItem--orders'
    ORDER_HISTORY_STATUS_LOCATOR='Нет заказов бумажных книг'
    ORDER_HISTORY_URL='https://www.litres.ru/me/orders/'



    def __init__(self, page: Page):
        super().__init__(page)

        self.username = page.get_by_test_id(self.PROFILE_NAME_LOCATOR) # это все локаты
        self.avatar = page.get_by_test_id(self.AVATAR_LOCATOR) # и это локаторы
        self.order_history = page.get_by_test_id(self.USER_ORDER_HISTORY_LOCATOR) #макс лох

    def go_to_history_by_url(self):
        self.page.goto(self.ORDER_HISTORY_URL)

    def go_to_user_history(self):
        self.order_history.click()

