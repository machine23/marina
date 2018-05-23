from django.urls import path

from . import views


app_name = 'quiz'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create', views.QuestionCreate.as_view(), name='create'),
    path('training', views.TrainingView.as_view(), name='training'),
]
