from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#вопрос
class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()

	author = models.OneToOneField(QuestionAuthor)
	likes = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

#ответ
class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	
	question = models.ForeignKey(Question, null=False, on_delete=models.CASCADE)
	author = models.OneToOneField(AnswerAuthor)

	
