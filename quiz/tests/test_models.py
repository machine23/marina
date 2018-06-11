import pytest
from mixer.backend.django import mixer

from quiz.models import Question, QuestionTheme

pytestmark = pytest.mark.django_db


class TestQuestionThemeModel:
    def test_saving_and_retrieving_theme(self):
        mixer.blend(QuestionTheme, title='question test theme')
        themes = QuestionTheme.objects.all()
        assert themes.count() == 1
        assert themes[0].title == 'question test theme'

    def test_title_max_length(self):
        mixer.blend(QuestionTheme)
        theme = QuestionTheme.objects.first()
        max_length = theme._meta.get_field('title').max_length
        assert max_length == 75

    def test_string_representation(self):
        mixer.blend(QuestionTheme, title='question theme')
        theme = QuestionTheme.objects.first()
        assert str(theme) == 'question theme'


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

    def test_text_field_label(self):
        question = mixer.blend(Question)
        field_label = question._meta.get_field('text').verbose_name
        assert field_label == 'Question'
