import sys
from datetime import datetime

sys.path.insert(0, '../lib/')
import requests

PINGDOM_BACKEND = 'https://api.pingdom.com/api/2.0'


class PingdomError(Exception):
    pass

class Pingdom(object):
    def __init__(self, email, password, api_key):
        self.email, self.password, self.api_key = email, password, api_key

    def get(self, path):
        headers = {'App-Key': self.api_key}
        resp = requests.get(PINGDOM_BACKEND + path, 
                            auth=(self.email, self.password), headers=headers)
        if resp.status_code != 200:
            raise PingdomError(resp.content)
        return resp.json()



API_KEY = 'xce4pti219pxnf2zehzfb4luidpuqizf'
EMAIL = 'gregdingle@yahoo.com'
PASSWORD = 'cloudywatch'

pingdom = Pingdom(EMAIL, PASSWORD, API_KEY)

all_checks = pingdom.get('/checks')

for check in all_checks['checks']:
    print check['id'], check['name']
    for probe in pingdom.get('/results/{0}?limit=5'.format(check['id']))['results']:
        print datetime.fromtimestamp(probe['time']).strftime('%Y-%m-%d %H:%M:%S'),
        print probe
