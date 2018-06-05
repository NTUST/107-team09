from django.contrib import admin

# Register your models here.
from .models import *

class QuestionInline(admin.TabularInline):
	model = Question

class QuestionSetAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'desc']}),
	]
	inlines = [QuestionInline]
	list_display = ('id', 'title')
	list_filter = ['title']
	search_fields = ['title']

admin.site.register(Question_Set, QuestionSetAdmin)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Mahou_Shoujo)
admin.site.register(Magic_Wand)
