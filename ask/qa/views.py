from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, HttpResponseRedirect
from datetime import date
from qa.models import *
from qa.paginator import paginate
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			ask = form.save()
			url = ask.get_absolute_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'qa/ask.html', {'form': form})		
	

@require_GET
def question(request, question_number):
	question = get_object_or_404(Question, id=question_number)
	since = request.GET.get('since')
	answers, since = Answer.objects.main(since, question)
	return render(request, 'qa/question.html',
				{
					'answers': answers,
					'question': question,
					'since': since
				})
		
@require_GET
def popular(request):
	questions = Question.objects.popular()
	page = paginate(request, questions)
	return render(request, 'qa/popular.html',
				{
					'questions': page.object_list,
					'page': page
				})

@require_GET
def home(request):
	questions = Question.objects.new()
	page = paginate(request, questions)
	return render(request, 'qa/home.html',
				{
					'questions': page.object_list,
					'page': page
				})

# Create your views here.
