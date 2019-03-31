import requests
from pprint import pprint
class HereMaps:
    def __init__(self, appId, appCode):
        self._appId = appId
        self._appCode = appCode
        self._baseUrl = 'https://places.api.here.com/places/v1'
        
    @property
    def baseUrl(self):
        return self._baseUrl
    
    def search(self, place):
        res = requests.get(self.baseUrl +
                           '/discover/search?app_id={}&app_code={}&at=-22.882219,-43.44194&q={}'.format(self._appId,
                                                                                                        self._appCode,
                                                                                                        place))
        return res.json()['results']['items']

    def beautifulsearch(self, place):
        res = requests.get(self.baseUrl +
                           '/discover/search?app_id={}&app_code={}&at=-22.882219,-43.44194&q={}'.format(self._appId,
                                                                                                        self._appCode,
                                                                                                        place))
        places = []

        for local in res.json()['results']['items']:
            parser = local['vicinity'].replace('<br/>', ', ')

            places.append({'Endereço': '{}, {}'.format(local['title'], parser),
                           'Latitude': local['position'][0],
                           'Longitude': local['position'][1]})

        return places
