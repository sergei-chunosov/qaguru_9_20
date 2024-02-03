from allure_commons._allure import step
from selene import browser, have
from utils.get_cookies import get_cookie, user_name
from utils.response import post_request


def test_login():
    cookies = get_cookie()

    with step('Open login page'):
        browser.open('')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})
        browser.open('')
        browser.element('.account').should(have.text(user_name))


def test_add_to_card():
    cookies = get_cookie()

    browser.open('')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})
    browser.open('')
    browser.element('.account').should(have.text(user_name))

    with step('Добавление товара в карзину'):
        url = '/addproducttocart/details/72/1'
        payload = {"product_attribute_72_5_18": 53,
                   "product_attribute_72_6_19": 54,
                   "product_attribute_72_3_20": 57,
                   "addtocart_72.EnteredQuantity": 1
                   }

        response = post_request(url, data=payload, cookies={'NOPCOMMERCE.AUTH': cookies})

    with step('Проверяем товар в корзине'):
        browser.open('cart')
        browser.element('.product-unit-price').should(have.text('815.00'))


def test_remove_from_card():
    cookies = get_cookie()

    browser.open('')
    browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})

    with step('Удаляем товар из карзины UI'):
        browser.open('')
        browser.driver.add_cookie({'name': 'NOPCOMMERCE.AUTH', 'value': cookies})
        browser.open('cart')
        browser.element('[name="removefromcart"]').click()
        browser.element('[name="updatecart"]').click()
        browser.all('.ico-cart span').second.should(have.text('(0)'))
