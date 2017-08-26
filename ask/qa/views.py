from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from qa.models import *
from qa.paginator import paginate


def test(request, *args, **kwargs):
	return HttpResponse('OK')

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
	paginator, page = paginate(request, questions, 'popular/?page=')
	return render(request, 'qa/popular.html',
				{
					'questions': page.object_list,
					'paginator': paginator,
					'page': page
				})

@require_GET
def home(request):
	questions = Question.objects.new()
	paginator, page = paginate(request, questions, '?page=')
	return render(request, 'qa/home.html',
				{
					'questions': page.object_list,
					'paginator': paginator,
					'page': page
				})

# Create your views here.
