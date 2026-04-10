from utils.config import Config

class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto(Config.BASE_URL)

    def login(self):
        self.page.fill("#user-name", Config.USERNAME)
        self.page.fill("#password", Config.PASSWORD)
        self.page.click("#login-button")