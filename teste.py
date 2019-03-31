from HereMaps import HereMaps
from Uber import Uber
from pprint import pprint
import datetime
from Configurations.Credentials import HereConf, UberConf

def timeConverter(time):
    return datetime.timedelta(seconds=time)


# HereMaps
here = HereConf()
appId = here.appId
appCode = here.appCode

# Uber
uber = UberConf()
serverToken = uber.serverToken


here = HereMaps(appId, appCode)
#locals = here.beautifulsearch('Rua Alexandre de Gusmão')

start = here.beautifulsearch('Rua Pedro Melo, 164, Padre Miguel')
if len(start) > 1:
    option = int(input('Choose a place [number]: '))
    start = start[option]
else:
    start = start[0]


end = here.beautifulsearch('Rua Alexandre de Gusmão, 28, Tijuca')
if len(end) > 1:
    option = int(input('Choose a place [number]: '))
    end = end[option]
else:
    end = end[0]

uber = Uber(serverToken)

prices = uber.price(start['Latitude'], start['Longitude'], end['Latitude'], end['Longitude'])

sheeper = [prices[0]]

for price in prices:
    if price['low_estimate'] < sheeper[0]['low_estimate']:
        sheeper.append(price)
        sheeper.pop(0)


print(timeConverter(555555555555))
