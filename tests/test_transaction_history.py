from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.transaction_page import TransactionPage


def test_transaction(page):

    # Login
    login = LoginPage(page)
    login.navigate()
    login.login()

    # Add product
    dashboard = DashboardPage(page)
    dashboard.add_to_cart()
    dashboard.go_to_cart()

    # Transaction
    transaction = TransactionPage(page)
    transaction.click_checkout()
    transaction.fill_details("Gowtham", "QA", "517001")
    transaction.finish_transaction()

    # Validation
    assert "Thank you" in transaction.get_success_message()