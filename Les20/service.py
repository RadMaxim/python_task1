import requests


def getAllDataFromBinance():
    try:
        data = requests.get("https://api.binance.com/api/v3/ticker/price")
        if data.status_code == 200:
            result = data.json()
            return result
    except:
        return []


def getAllDataColor():
    try:
        data = requests.get("https://695bbd7e1d8041d5eeb835fd.mockapi.io/api/v1/leds")
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
    except:
        return {}


token = getTokenFromBinance("BTCUSDT")


def getOnlyNamesCrypto():
    data = getAllDataFromBinance()
    names = list(
        map(
            lambda crypto: crypto["symbol"],
            data,
        )
    )[:20]
    return names


def getDataFromMockAPI():
    try:
        response = requests.get("https://695bbd7e1d8041d5eeb835fd.mockapi.io/api/v1/leds")

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("status is not 200")
            return []
    except:
        print("Mistake of request")
        return []
