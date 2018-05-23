from django.urls import reverse
from mixer.backend.django import mixer
import pytest

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
        assert 'quiz/index.html' in used_templates
        assert 'Hello from Marina' in resp.content.decode()

    def test_index_view_displays_questions_count(self, client):
        mixer.cycle(5).blend('quiz.Question')
        resp = client.get(reverse('quiz:index'))
        assert resp.status_code == 200
        assert resp.context['questions_count'] == 5
