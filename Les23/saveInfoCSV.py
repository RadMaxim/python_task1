import csv


def createCSV():
    with open(
        "data.csv",
        "w",
        newline="",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                "Время",
                "Повторение",
                "Угол",
                "Глубина",
            ]
        )


def addData(
    time="00:00",
    rating=1,
):

    with open(
        "data.csv",
        "a",
        newline="",
    ) as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                time,
                rating,
            ]
        )


print("Готово! Файл data.csv создан")
