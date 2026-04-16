import requests


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


result = getDataFromMockAPI()
print(result)
