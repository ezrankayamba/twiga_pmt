from django.db import models


class AwardSession(models.Model):
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


class Win(models.Model):
    title = models.CharField(max_length=100)
    winner = models.CharField(max_length=100)
    award_session = models.ForeignKey(to=AwardSession, on_delete=models.CASCADE)
    announced = models.BooleanField(default=False)


class Fact(models.Model):
    name = models.CharField(max_length=200)
    win = models.ForeignKey(to=Win, on_delete=models.CASCADE)
