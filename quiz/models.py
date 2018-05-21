from django.db import models


class Question(models.Model):
    text = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
