from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView
from quiz.models import Question
from django.urls import reverse_lazy
from django.http import HttpResponse


class IndexView(TemplateView):
    template_name = 'quiz/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions_count'] = Question.objects.count()
        return context


class QuestionCreate(CreateView):
    template_name = 'quiz/create.html'
    model = Question
    fields = ['text', 'answer']
    success_url = reverse_lazy('quiz:create')


class TrainingView(View):
    def get(self, request):
        return HttpResponse('Training')
