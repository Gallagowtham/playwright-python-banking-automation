class TransactionPage:

    def __init__(self, page):
        self.page = page

    def open_menu(self):
        self.page.click("#react-burger-menu-btn")

    def go_to_orders(self):
        self.page.click("#inventory_sidebar_link")

    def open_cart(self):
        self.page.click(".shopping_cart_link")

    def click_checkout(self):
        self.page.click("#checkout")

    def fill_details(self, first_name, last_name, zip_code):
        self.page.fill("#first-name", first_name)
        self.page.fill("#last-name", last_name)
        self.page.fill("#postal-code", zip_code)
        self.page.click("#continue")

    def finish_transaction(self):
        self.page.click("#finish")

    def get_success_message(self):
        return self.page.text_content(".complete-header")