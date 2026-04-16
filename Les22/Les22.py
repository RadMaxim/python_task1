import random
import time

import requests

urlMockApi = "https://697f289bd1548030ab654a3b.mockapi.io/api/yaroslav"
colors = [
    "red",
    "green",
    "blue",
]
for i in range(
    0,
    50,
):
    time.sleep(1)
    timer = random.randint(
        100,
        2000,
    )
    colorI = random.randint(
        0,
        2,
    )
    data = requests.post(
        urlMockApi,
        json={
            "timer": timer,
            "color": colors[colorI],
        },
    )
