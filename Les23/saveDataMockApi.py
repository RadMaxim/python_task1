import requests

urlMockApi = "https://697f289bd1548030ab654a3b.mockapi.io/api/yaroslav"
count_reserve = 0


def saveData(
    time,
    rating,
):
    global count_reserve
    try:
        requests.post(
            urlMockApi,
            json={
                "timer": time,
                "rating": rating,
            },
        )
    except:
        print("Ошибка в сохранении приседа, сохраняем локально")
        count_reserve += 1


def getStatistic():
    try:
        data = requests.get(urlMockApi)
        if data.status_code == 200:
            result = data.json()
            ratings = [item["rating"] for item in result]
            average_rating = sum(ratings) / len(ratings)
            print(f"Средний рейтинг: {average_rating:.2f}")

        else:
            print("Ошибка получения статистики")
    except:
        print("")
