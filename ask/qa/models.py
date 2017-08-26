from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-added_at")
	
	def popular(self):
		return self.order_by("-rating")


class AnswerManager(models.Manager):
	def main(self, since, question, limit=10):
		qs = self.order_by("-added_at")
		qs = qs.filter(question=question)
		res = []
		if since is not None and since != "None":
			qs = qs.filter(added_at__lt=since)
		for p in qs[:100]:
			res.append(p)
			if len(res) >= limit:
				break
		if len(res) > 1:
			since = res[-1].added_at
		elif len(res) == 1:
			since = res[0].added_at
		return res, since


class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)

	author = models.OneToOneField(User)
	likes = models.ManyToManyField(User, related_name="question_like_user")
	objects = QuestionManager()


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	
	question = models.ForeignKey(Question, null=False)
	author = models.OneToOneField(User)
	objects = AnswerManager()

	
