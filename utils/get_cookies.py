import requests
from dotenv import load_dotenv
import os

load_dotenv()
user_name = os.environ.get('LOGIN')
password = os.environ.get('PASSWORD')


def get_cookie():
    url = 'https://demowebshop.tricentis.com/login'
    payload = {"Email": user_name, "Password": password, "RememberMe": "false"}
    response = requests.post(url, data=payload, allow_redirects=False)
    cookies = response.cookies.get('NOPCOMMERCE.AUTH')
    return cookies


print(get_cookie())
