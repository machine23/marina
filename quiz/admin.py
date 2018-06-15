from django.contrib import admin
from quiz.models import Question, QuestionTheme


admin.site.register(QuestionTheme)
admin.site.register(Question)
