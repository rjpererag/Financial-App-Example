import requests
from typing import Any
from requests.exceptions import RequestException
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type

from .abstract import AbstractEndpointRequestor


class EndpointRequestor(AbstractEndpointRequestor):

    def __init__(self):
        ...

    @retry(
        retry=retry_if_exception_type(RequestException),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=1, min=1, max=10)
    )
    def get(self, url: str, headers: dict, params: dict) -> dict:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()

    def post(self) -> Any:
        ...

    def put(self) -> Any:
        ...

    def delete(self) -> Any:
        ...
