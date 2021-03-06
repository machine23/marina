import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from quiz.models import Question
from quiz.forms import QuizForm

pytestmark = pytest.mark.django_db


class TestIndexView:
    def test_index_view_exists(self, client):
        resp = client.get('/')
        assert resp.status_code == 200

    def test_index_view_url_accessible_by_name(self, client):
        resp = client.get(reverse('quiz:index'))
        assert resp.status_code == 200

    def test_index_view_uses_correct_template(self, client):
        resp = client.get(reverse('quiz:index'))
        used_templates = [template.name for template in resp.templates]
        assert 'base.html' in used_templates
        assert 'quiz/index.html' in used_templates
        assert 'Hello from Marina' in resp.content.decode()

    def test_index_view_displays_questions_count(self, client):
        mixer.cycle(5).blend('quiz.Question')
        resp = client.get(reverse('quiz:index'))
        assert resp.status_code == 200
        assert resp.context['questions_count'] == 5


class TestCreateView:
    def test_create_view_exists(self, client):
        resp = client.get('/create')
        assert resp.status_code == 200

    def test_create_view_url_accessible_by_name(self, client):
        resp = client.get(reverse('quiz:create'))
        assert resp.status_code == 200

    def test_createview_uses_correct_template(self, client):
        resp = client.get(reverse('quiz:create'))
        used_templates = [template.name for template in resp.templates]
        assert 'base.html' in used_templates
        assert 'quiz/create.html' in used_templates

    def test_post(self, client):
        data = {
            'text': 'Question text 1',
            'answer': 'Answer text 1',
        }
        resp = client.post(reverse('quiz:create'), data=data)
        assert resp.status_code == 302
        assert resp.url == reverse('quiz:create')
        question = Question.objects.first()
        assert question.text == 'Question text 1'
        assert question.answer == 'Answer text 1'


class TestTrainingView:
    def test_trainingview_exists(self, client):
        resp = client.get('/training')
        assert resp.status_code == 200

    def test_trainingview_url_accessible_by_name(self, client):
        resp = client.get(reverse('quiz:training'))
        assert resp.status_code == 200

    def test_trainingview_uses_correct_template(self, client):
        resp = client.get(reverse('quiz:training'))
        used_templates = {template.name for template in resp.templates}
        expect_templates = {'base.html', 'quiz/training.html'}
        assert used_templates == expect_templates

    def test_quizform_in_context(self, client):
        response = client.get(reverse('quiz:training'))
        assert 'form' in response.context
        assert isinstance(response.context['form'], QuizForm)


class TestQuestionView:
    def test_get(self, client):
        question = mixer.blend('quiz.Question')
        response = client.get(reverse('quiz:question'))
        expect = {
            'question': question.text,
            'answer': question.answer,
        }
        assert response.status_code == 200
        assert response.json() == expect

    def test_get_repeat_if_only_one_question_in_db(self, client):
        mixer.blend('quiz.Question')
        response1 = client.get(reverse('quiz:question'))
        response2 = client.get(reverse('quiz:question'))
        assert response1.json() == response2.json()

    def test_get_no_repeat(self, client):
        mixer.cycle(2).blend('quiz.Question')
        response1 = client.get(reverse('quiz:question'))
        response2 = client.get(reverse('quiz:question'))
        assert response1.json() != response2.json()
