from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Question_Set(models.Model):
	title = models.CharField(max_length = 50)
	desc = models.CharField(max_length = 150) #描述
	def __str__(self):
		return self.title
class Question(models.Model):
	text = models.CharField(max_length = 150)
	question_set = models.ForeignKey(Question_Set,on_delete = models.CASCADE)
	def __str__(self):
		return self.text
class Option(models.Model):
	text = models.CharField(max_length = 150)
	op_type = models.CharField(max_length = 1, default="")
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
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
	mahou_shoujo = models.ForeignKey(Mahou_Shoujo,on_delete = models.CASCADE)
	def __str__(self):
		return self.name
class User_Mahou_Shoujo(models.Model):
	creation_time = models.DateTimeField(default = timezone.now)
	mahou_shoujo = models.ForeignKey(Mahou_Shoujo,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
class User_Question_Set(models.Model):
	op_type = models.CharField(max_length = 1, default="")
	question_Set = models.ForeignKey(Question_Set,on_delete = models.CASCADE)
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	creation_time = models.DateTimeField(default = timezone.now)

		