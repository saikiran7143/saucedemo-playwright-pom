from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_valid_login_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        assert "inventory" in page.url
        browser.close()

def test_locked_out_login_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        assert "Sorry, this user has been locked out." in login_page.get_error_text()
        browser.close()

from pages.inventory_page import InventoryPage

def test_add_to_cart_pom():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(page)
        inventory_page.add_backpack_to_cart()
        inventory_page.open_cart()

        assert inventory_page.get_cart_item_name() == "Sauce Labs Backpack"
        browser.close()
