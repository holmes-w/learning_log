from django import forms
from learning_logs.models import Topic, Entry


class TopicForms(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'tetx': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}