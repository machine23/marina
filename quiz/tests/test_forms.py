from django import forms

from quiz.forms import QuestionForm, QuizForm


class TestQuestionForm:
    def setup_method(self, method):
        self.form = QuestionForm()

    def test_question_form_is_form(self):
        assert issubclass(QuestionForm, forms.ModelForm)

    def test_text_field(self):
        assert 'text' in self.form.fields
        assert self.form.fields['text'].label == 'Question'

    def test_question_form_labels(self):
        assert 'answer' in self.form.fields
        assert self.form.fields['answer'].label == 'Answer'


class TestQuizForm:
    def setup_method(self, method):
        self.form = QuizForm()

    def test_form_is_form(self):
        assert issubclass(QuizForm, forms.Form)

    def test_answer_field(self):
        assert 'answer' in self.form.fields
        assert isinstance(self.form.fields['answer'].widget, forms.Textarea)
