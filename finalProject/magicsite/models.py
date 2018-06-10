from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Question_Set(models.Model):
	title = models.CharField(max_length=50)
	desc = models.CharField(max_length=150)

	def __str__(self):
		return self.title

class Question(models.Model):
	question_set = models.ForeignKey(Question_Set, on_delete=models.CASCADE)
	text = models.CharField(max_length = 150)
	
	def __str__(self):
		return self.text

class Option(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	text = models.CharField(max_length=150)
	op_type = models.CharField(max_length=1, default="")

	def __str__(self):
		return self.text

class Mahou_Shoujo(models.Model):
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=500)
	image = models.ImageField(upload_to='photos', null=True, default=None) 
	age = models.DecimalField(max_digits = 4,decimal_places = 0)

	def __str__(self):
		return self.name

class Magic_Wand(models.Model):
	mahou_shoujo = models.ForeignKey(Mahou_Shoujo, on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	desc = models.CharField(max_length=500)
	image = models.ImageField(upload_to='photos', null=True, default=None) 
	
	def __str__(self):
		return self.name

class User_Mahou_Shoujo(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	question_set = models.ForeignKey(Question_Set, on_delete=models.CASCADE, null=True)
	mahou_shoujo = models.ForeignKey(Mahou_Shoujo, on_delete=models.CASCADE)
	creation_time = models.DateTimeField(default=timezone.now)
	
	def __str__(self):
		return self.user.__str__() + '_' + self.question_set.__str__() + '_' + self.mahou_shoujo.__str__()
		