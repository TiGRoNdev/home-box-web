from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from qa.models import QuestionManager
from qa.paginator import paginate


def test(request, *args, **kwargs):
	return HttpResponse('OK')

def question(request, question_number):
	pass

def popular(request):
	pass

def home(request):
	questions = QuestionManager.new()
	paginator, page = paginate(request, questions, '?page=')
	return render(request, 'qa/home.html',
				{
					'questions': page.object_list,
					'paginator': paginator,
					'page': page
				})

# Create your views here.
