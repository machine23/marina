import pytest
from django.urls import reverse
from mixer.backend.django import mixer

from quiz.models import Question

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
