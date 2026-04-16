from django.db import (
    models,
)


class Rating(models.Model):
    timer = models.CharField(max_length=50)  # Время (например: "10:00")
    rating = models.FloatField()  # Оценка (например: 4.5)
    user_id = models.IntegerField()  # ID пользователя
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания

    def __str__(
        self,
    ):
        return f"{self.timer} - {self.rating}"
