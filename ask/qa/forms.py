from django import forms
from qa.models import Question, Answer


class AskForm(forms.Form):
	title = forms.CharField(max_length=100, initial='Your Question')
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		text = self.cleaned_data['text']
		if len(text) > 1000:
			raise forms.ValidationError('Symbols in text > 1000')
		return self.cleaned_data
	
	def save(self):
		question = Question.objects.create_question(self.cleaned_data)
		question.save()
		return question


class AnswerForm(forms.Form):
	def all_choices():
		def get_tuple(obj):
			return (str(obj), str(obj))
		qs = Question.objects.all()
		return tuple(map(get_tuple, qs))

	question = forms.ChoiceField(choices=all_choices(), initial='Choose the question')
	text = forms.CharField(max_length=600, widget=forms.Textarea, initial='Your answer')
	
	def clean_question(self):
		question = self.cleaned_data['question']
		try:
			test_question = Question.objects.get(title=str(question))
		except Question.DoesNotExist:
			raise forms.ValidationError('Question with this title does not exist')
		return test_question
	
	def save(self):
		answer = Answer.objects.create_answer(self.cleaned_data)
		answer.save()
		return answer
