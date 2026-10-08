import time
from selenium.webdriver.common.by import By


def test_button_add_to_basket_exists(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза по требованию задания — чтобы визуально проверить язык кнопки
    time.sleep(30)

    # Ищем кнопку добавления в корзину
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Проверяем, что кнопка есть
    assert button is not None, "Кнопка 'Add to basket' не найдена на странице"