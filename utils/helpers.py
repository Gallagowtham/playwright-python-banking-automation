import time
from playwright.sync_api import expect


class Helpers:

    @staticmethod
    def wait_for_element(page, locator):
        page.wait_for_selector(locator)


    @staticmethod
    def click_element(page, locator):
        page.locator(locator).click()


    @staticmethod
    def fill_text(page, locator, text):
        page.locator(locator).fill(text)


    @staticmethod
    def get_text(page, locator):
        return page.locator(locator).text_content()


    @staticmethod
    def take_screenshot(page, name):
        page.screenshot(path=f"screenshots/{name}.png")


    @staticmethod
    def wait_for_url(page, url):
        page.wait_for_url(url)


    @staticmethod
    def wait_for_load(page):
        page.wait_for_load_state("networkidle")


    @staticmethod
    def assert_text(page, locator, text):
        expect(page.locator(locator)).to_have_text(text)