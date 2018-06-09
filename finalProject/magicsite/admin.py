from django.contrib import admin

# Register your models here.
from .models import *

class QuestionInline(admin.TabularInline):
	model = Question
class OptionInline(admin.TabularInline):
	model = Option
class Magic_WandInline(admin.TabularInline):
	model = Magic_Wand


class QuestionSetAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'desc']}),
	]
	inlines = [QuestionInline]
	list_display = ('id', 'title')
	list_filter = ['title']
	search_fields = ['title']
class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_set', 'text']}),
	]
	inlines = [OptionInline]
	list_display = ('id', 'question_set')
	list_filter = ['question_set']
	search_fields = ['question_set']
class MahouShoujoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'desc']}),
	]
	inlines = [Magic_WandInline]
	list_display = ('id', 'name')
	list_filter = ['name']
	search_fields = ['name']

admin.site.register(Question_Set, QuestionSetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option)
admin.site.register(Mahou_Shoujo, MahouShoujoAdmin)
admin.site.register(Magic_Wand)
admin.site.register(User_Mahou_Shoujo)
admin.site.register(User_Question_Set)