import requests
import urls

def getApi(barcode: str):
    res = requests.get(urls.KERRY_API + barcode + '/th')
    return res.json()