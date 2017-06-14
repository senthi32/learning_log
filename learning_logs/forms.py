# This is forms.py
from django import forms
from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta: 
		model = Topic
		fields = ['text']
		labels = {'text':'Your New Topic'}

class EntryForm(forms.ModelForm):
	class Meta: 
		model = Entry
		fields = ['text']
		labels = {'text':''}
		widgets = {'text': forms.Textarea(attrs={'col':80})}
