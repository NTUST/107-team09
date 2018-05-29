from django.db import models

# Create your models here.
class Question_Set(models.Model):
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150) #描述
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
class Mahou_Shoujo(models.Model):
	name = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 500) #描述
	image = models.ImageField(upload_to='photos', null=True, default=None) 
	age = models.DecimalField(max_digits = 4,decimal_places = 0)
	def __str__(self):
		return self.name
class Magic_Wand(models.Model):
	name = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 500) #描述
	image = models.ImageField(upload_to='photos', null=True, default=None) 
	mahou_shoujo = models.ForeignKey(Mahou_Shoujo)
	def __str__(self):
		return self.name
