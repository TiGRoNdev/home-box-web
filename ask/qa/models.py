from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by("-id")
	
	def popular(self):
		return self.order_by("-rating")


class AnswerManager(models.Manager):
	def main(self, since, question, limit=10):
		qs = self.order_by("-id")
		qs = qs.filter(question=question)
		res = []
		if since is not None and since != "None":
			qs = qs.filter(id__lt=since)
		for p in qs[:100]:
			res.append(p)
			if len(res) >= limit:
				break
		if len(res) > 1:
			since = res[-1].id
		elif len(res) == 1:
			since = res[0].id
		return res, since


class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	rating = models.IntegerField(default=0)

	author = models.ForeignKey(User, null=False, default=1)
	likes = models.ManyToManyField(User, related_name="question_like_user")
	objects = QuestionManager()


class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField(blank=True, auto_now_add=True)
	
	question = models.ForeignKey(Question, null=False)
	author = models.ForeignKey(User, null=False, default=1)
	objects = AnswerManager()

	
