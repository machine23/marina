from quiz.models import Question
from django.test import TestCase


class TestQuestionModel(TestCase):
    def test_saving_and_retrieving_questions(self):
        first_question = Question()
        first_question.text = 'The first question'
        first_question.save()

        second_question = Question()
        second_question.text = 'The second question'
        second_question.save()

        saved_questions = Question.objects.all()

        assert saved_questions.count() == 2

        first_saved_question = saved_questions[0]
        second_saved_question = saved_questions[1]
        assert first_saved_question.text == 'The first question'
        assert second_saved_question.text == 'The second question'

    def test_string_representation(self):
        question = Question(text='question text')
        assert str(question) == question.text
