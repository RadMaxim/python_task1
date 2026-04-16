from django.db import (
    models,
)


class Rating(models.Model):
    timer = models.CharField(max_length=50)
    rating = models.FloatField()
    user_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(
        self,
    ):
        return f"{self.timer} - {self.rating}"
