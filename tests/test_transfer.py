class TransferPage:

    def __init__(self, page):
        self.page = page

    def add_product(self):
        self.page.locator(".inventory_item button").first.click()

    def go_to_cart(self):
        self.page.click(".shopping_cart_link")

    def click_checkout(self):
        self.page.click("#checkout")

    def enter_transfer_details(self, first_name, last_name, zip_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def confirm_transfer(self):
        self.page.click("#finish")

    def get_success_message(self):
        return self.page.text_content(".complete-header")