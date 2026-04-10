class PaymentPage:

    def __init__(self, page):
        self.page = page

    def checkout(self):
        self.page.click("#checkout")

    def enter_details(self):
        self.page.fill("#first-name", "Gowtham")
        self.page.fill("#last-name", "QA")
        self.page.fill("#postal-code", "517001")
        self.page.click("#continue")

    def finish(self):
        self.page.click("#finish")

    def get_success_message(self):
        return self.page.text_content(".complete-header")