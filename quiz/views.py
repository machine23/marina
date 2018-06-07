from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from django.views.generic.edit import CreateView

from quiz.forms import QuizForm
from quiz.models import Question


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
        question = Question.objects.first()
        if question:
            request.session['question_id'] = question.id
        form = QuizForm()
        context = {
            'question': question,
            'form': form,
        }
        return render(request, 'quiz/training.html', context)
