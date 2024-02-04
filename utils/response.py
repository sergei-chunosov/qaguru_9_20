import logging
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import curlify


def post_request(url, data, cookies):
    base_url = "https://demowebshop.tricentis.com"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, data=data, cookies=cookies)
        curl = curlify.to_curl(response.request)
        print(curl)
        logging.info(curlify.to_curl(response.request))
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
