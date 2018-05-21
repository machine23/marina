from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):
    def test_index_view_exists(self):
        resp = self.client.get('/')
        assert resp.status_code == 200

    def test_index_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('quiz:index'))
        assert resp.status_code == 200

    def test_index_view_uses_correct_template(self):
        resp = self.client.get(reverse('quiz:index'))
        self.assertTemplateUsed(resp, 'quiz/index.html')
