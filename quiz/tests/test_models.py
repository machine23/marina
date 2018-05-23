import pytest
from mixer.backend.django import mixer

from quiz.models import Question

pytestmark = pytest.mark.django_db


class TestQuestionModel:
    def test_saving_and_retrieving_questions(self):
        mixer.blend(
            Question, text='The first question', answer='The first answer')

        Question.objects.create(text='The second question', )

        saved_questions = Question.objects.all()

        assert saved_questions.count() == 2

        first_saved_question = saved_questions[0]
        second_saved_question = saved_questions[1]
        assert first_saved_question.text == 'The first question'
        assert first_saved_question.answer == 'The first answer'
        assert second_saved_question.text == 'The second question'
        assert second_saved_question.answer == ''

    def test_string_representation(self):
        question = Question(text='question text')
        assert str(question) == question.text
