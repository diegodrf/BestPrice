from uber_rides.session import Session
from uber_rides.client import UberRidesClient
from pprint import pprint
import requests

class Uber:
    def __init__(self, serverToken):
        self._serverToken = serverToken
        self._baseUrl = 'https://api.uber.com/v1.2'

    @property
    def baseUrl(self):
        return self._baseUrl

    def go(self):
        session = Session(server_token=self._serverToken)
        client = UberRidesClient(session)
        response = client.get_products(37.77, -122.41)
        products = response.json
        return products

    def price(self, startLatitude, startLongitude, endLatitude, endLongitude):
        headers = {'Authorization': 'Token {}'.format(self._serverToken),
                  'Accept-Language': 'en_US',
                   'Content-Type': 'application/json'}

        url = self.baseUrl + \
              '/estimates/price?' \
              'start_latitude={}&start_longitude={}' \
              '&end_latitude={}&end_longitude={}'.format(startLatitude, startLongitude, endLatitude, endLongitude)

        res = requests.get(url, headers=headers)
        return res.json()['prices']


if __name__ == '__main__':
    serverToken = 'n9ANFCoeUpii3f5F0FqUumZ7Q23YXhvaxGTTlL6V'

    uber = Uber(serverToken)
    pprint(uber.price(-22.92506, -43.228939, -22.882219, -43.44194))
