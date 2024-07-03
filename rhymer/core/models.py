from django.db import models


class AllWords(models.Model):
    word = models.CharField(max_length=150)

    def __str__(self):
        return self.word
