import requests


def getAllDataFromBinance():
    try:
        req = requests.get("https://api.binance.com/api/v3/ticker/price")
        if req.status_code == 200:
            data = req.json()
            return data
    except Exception as e:
        print(e)
        return []
    finally:
        print("finish")


def getSymbolDataFromBinance(
    symbol,
):
    try:
        if str(symbol).strip() == "":
            raise ValueError("Data is empty")

        req = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
        if req.status_code != 200:
            raise ValueError("status is not 200")
        data = req.json()
        return data
    except Exception as e:
        print(e)
        return {}
    finally:
        print("finish")
