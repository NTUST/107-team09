from django.db import models

# Create your models here.
class Question_Set(models.Model):
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150)
	def __str__(self):
		return self.title
class Question(models.Model):
	text = models.CharField(max_length = 150)
	question_set = models.ForeignKey(Question_Set)
	def __str__(self):
		return self.text
class Option(models.Model):
	text = models.CharField(max_length = 150)
	score = models.DecimalField(max_digits = 6,decimal_places = 3)
	question = models.ForeignKey(Question)
	def __str__(self):
		return self.text
