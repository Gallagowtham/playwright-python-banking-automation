from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.payment_page import PaymentPage

def test_payment(page):

    login = LoginPage(page)
    login.navigate()
    login.login()

    dashboard = DashboardPage(page)
    dashboard.add_to_cart()
    dashboard.go_to_cart()

    payment = PaymentPage(page)
    payment.checkout()
    payment.enter_details()
    payment.finish()

    assert "Thank you" in payment.get_success_message()