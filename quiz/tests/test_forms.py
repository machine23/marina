from django import forms

from quiz.forms import QuestionForm


class TestQuestionForm:
    def test_question_form_is_form(self):
        assert issubclass(QuestionForm, forms.ModelForm)

    def test_question_form_fields(self):
        form = QuestionForm()
        assert len(form.fields) == 2
        assert list(form.fields) == ['text', 'answer']

    def test_question_form_labels(self):
        form = QuestionForm()
        assert form.fields['text'].label == 'Question'
        assert form.fields['answer'].label == 'Answer'
