import urllib3
import json
import os


API_KEY = os.environ["API_KEY"]
my_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/MXN"


def lambdaHandler(event, context):

    r = http.request('GET', my_url)
    response = json.loads(r.data.decode('utf-8'))
    mexicanPeso = response["conversion_rate"]

    return mexicanPeso
