from django import forms

from quiz.models import Question


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'answer']


class QuizForm(forms.Form):
    answer = forms.CharField(widget=forms.Textarea)
