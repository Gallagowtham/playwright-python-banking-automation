from pages.login_page import LoginPage

def test_login(page):

    login = LoginPage(page)
    login.navigate()
    login.login()

    assert "inventory" in page.url