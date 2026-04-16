import requests


def everyToken(
    arr,
):
    for crypto in arr:
        print(crypto)


def getAllDataFromBinance():
    try:
        data = requests.get("https://api.binance.com/api/v3/ticker/price")
        if data.status_code == 200:
            result = data.json()
            return result
        else:
            return []
    except:
        return []


def getTokenFromBinance(
    symbol,
):
    try:
        data = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        if data.status_code == 200:
            result = data.json()
            return result
        else:
            return []
    except:
        return {}


token = getTokenFromBinance("BTCUSDT")
print(token)
