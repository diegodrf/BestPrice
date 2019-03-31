from flask import Flask, request, render_template, url_for
from HereMaps import HereMaps
from Uber import Uber
import datetime
from Configurations.Credentials import HereConf, UberConf

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('formulario.html')

@app.route('/prices', methods=['POST'])
def prices():
    startForm = request.form['start']
    endForm = request.form['end']

    #### Begin ####
    # HereMaps
    here = HereConf()
    appId = here.appId
    appCode = here.appCode

    # Uber
    uber = UberConf()
    serverToken = uber.serverToken

    here = HereMaps(appId, appCode)

    start = here.beautifulsearch(startForm)
    end = here.beautifulsearch(endForm)

    if (len(start) > 1) or (len(end) > 1):
        return render_template('choice.html', start=start, end=end)

    uber = Uber(serverToken)
    prices = uber.price(start[0]['Latitude'], start[0]['Longitude'], end[0]['Latitude'], end[0]['Longitude'])

    #### END ####

    sheeper = [prices[0]]

    for price in prices:
        if price['low_estimate'] < sheeper[0]['low_estimate']:
            sheeper.append(price)
            sheeper.pop(0)

    return render_template('result.html', prices=sheeper, start=start, end=end)

@app.route('/choice', methods=['POST'])
def choice():
    return render_template(url_for(prices))


def timeConverter(time):
    return datetime.timedelta(seconds=time)


app.jinja_env.filters['timeConverter'] = timeConverter

app.run(debug=True, host='0.0.0.0')
