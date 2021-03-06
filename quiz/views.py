import random

from django.http import JsonResponse
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
        form = QuizForm()
        context = {
            'form': form,
        }
        return render(request, 'quiz/training.html', context)


class QuestionView(View):
    def get(self, request):
        print(request.COOKIES)
        questions = Question.objects.all()
        if questions.count() > 1:
            while True:
                question = random.choice(questions)
                if request.session.get('question_id') != question.id:
                    break
        else:
            question = questions.first()
        request.session['question_id'] = question.id
        data = {
            'question': question.text,
            'answer': question.answer,
        }
        return JsonResponse(data)
