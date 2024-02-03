import logging
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
import curlify


def post_request(url, **kwargs):
    base_url = "https://demowebshop.tricentis.com"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curlify.to_curl(response.request))
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response
