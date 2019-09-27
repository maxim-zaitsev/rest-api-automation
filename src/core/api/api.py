import json

import requests
from src.core.helpers.logger import Logger


class API(Logger):

    def __init__(self):
        super().__init__()
        self._hostname = ''
        self._cookies = {}
        self._headers = {}

    def _set_hostname(self, value):
        self._hostname = value

    def get_hostname(self):
        return self._hostname

    def set_cookies(self, key, value):
        self._cookies[key] = value

    def get_cookies(self):
        return self._cookies

    def get_cookie_by_name(self, value):
        return self.get_cookies().get(value)

    def post(self, api, data):
        api_call = self.get_hostname() + api
        response = requests.post(api_call, data)
        self.log('sending POST, url: {}, data: {}'.format(api_call, data))
        self.log('status code: {}'.format(response.status_code))
        response_data = json.loads(response.content)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def put(self, api, data):
        api_call = self.get_hostname() + api
        response = requests.put(api_call, data)
        self.log('sending PUT, url: {}, data: {}'.format(api_call, data))
        self.log('status code: {}'.format(response.status_code))
        response_data = json.loads(response.content)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def get(self, api):
        api_call = self.get_hostname() + api
        response = requests.get(api_call)
        self.log('sending GET, url: {}'.format(api_call))
        self.log('status code: {}'.format(response.status_code))
        response_data = json.loads(response.content)
        self.log('response data: {}'.format(response_data))
        return response, response_data

    def delete(self, api):
        api_call = self.get_hostname() + api
        response = requests.get(api_call)
        self.log('sending DELETE, url: {}'.format(api_call))
        self.log('status code: {}'.format(response.status_code))
        response_data = json.loads(response.content)
        self.log('response data: {}'.format(response_data))
        return response, response_data
