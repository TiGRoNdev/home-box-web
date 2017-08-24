from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#вопрос
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	rating = models.IntegerField()

	author = models.OneToOneField(QuestionAuthor)
	likes = models.ManyToManyField(User, null=True, on_delete=models.SET_NULL, related_name="question_like_user")
	objects = QuestionManager()

class QuestionManager(models.Manager):
	

#ответ
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(auto_now_add=True)
	
	question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
	author = models.OneToOneField(AnswerAuthor)

	
