from botocore.vendored import requests
import os


API_KEY = os.environ["API_KEY"]
my_url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/MXN"


def lambdaHandler(event, context):

    r = requests.get(my_url)
    apiResponse = r.json()
    mexicanPeso = apiResponse["conversion_rate"]

    return mexicanPeso
