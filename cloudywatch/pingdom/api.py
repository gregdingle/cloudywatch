import requests
from django.conf import settings


PINGDOM_BACKEND = 'https://api.pingdom.com/api/2.0'


class PingdomError(Exception):
    pass


class Pingdom(object):
    def __init__(self, email, password, api_key):
        self.email, self.password, self.api_key = email, password, api_key

    def get(self, path):
        headers = {'App-Key': self.api_key}
        try:
            resp = requests.get(PINGDOM_BACKEND + path,
                                auth=(self.email, self.password), headers=headers, timeout=30)
        except requests.exceptions.Timeout:
            raise PingdomError("Connection timeout.")

        if resp.status_code != 200:
            raise PingdomError(resp.content)
        return resp.json()


pingdom = Pingdom(settings.PINGDOM_EMAIL, settings.PINGDOM_PASSWORD, settings.PINGDOM_API_KEY)
