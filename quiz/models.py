from django.db import models


class QuestionTheme(models.Model):
    title = models.CharField(max_length=75)

    def __str__(self):
        return self.title


class Question(models.Model):
    theme = models.ForeignKey(QuestionTheme, on_delete=models.CASCADE, blank=True, null=True)
    text = models.TextField('Question')
    answer = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
