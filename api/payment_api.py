import requests

def get_payment_status():

    url = "https://jsonplaceholder.typicode.com/posts/1"

    response = requests.get(url)

    return response.status_code