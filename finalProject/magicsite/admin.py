from django.contrib import admin

# Register your models here.
from .models import *

class QuestionInline(admin.TabularInline):
	model = Question

class OptionInline(admin.TabularInline):
	model = Option

class Magic_WandInline(admin.TabularInline):
	model = Magic_Wand

class User_Mahou_ShoujoInline(admin.TabularInline):
	model = User_Mahou_Shoujo

class QuestionSetAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['title', 'desc']}),
	]
	inlines = [QuestionInline, User_Mahou_ShoujoInline]
	list_display = ('id', 'title')
	list_filter = ['title']
	search_fields = ['title']

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_set', 'text']}),
	]
	inlines = [OptionInline]
	list_display = ('id', 'question_set', 'text')
	list_filter = ['question_set']
	search_fields = ['question_set']

class OptionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question', 'text', 'op_type']}),
	]
	list_display = ('id', 'question', 'text', 'op_type')
	list_filter = ['question']
	search_fields = ['question']

class MahouShoujoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['name', 'desc']}),
	]
	inlines = [Magic_WandInline, User_Mahou_ShoujoInline]
	list_display = ('id', 'name', 'desc')
	list_filter = ['name']
	search_fields = ['name']

class MagicWandAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['mahou_shoujo', 'name', 'desc', 'image']}),
	]
	list_display = ('id', 'name', 'desc', 'mahou_shoujo')
	list_filter = ['mahou_shoujo']
	search_fields = ['mahou_shoujo']

class UserMahouShoujoAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['user', 'question_set', 'mahou_shoujo', 'creation_time']}),
	]
	list_display = ('id', 'user', 'question_set', 'mahou_shoujo')
	list_filter = ['user', 'question_set', 'mahou_shoujo']
	search_fields = ['user', 'question_set', 'mahou_shoujo']

admin.site.register(Question_Set, QuestionSetAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(Mahou_Shoujo, MahouShoujoAdmin)
admin.site.register(Magic_Wand, MagicWandAdmin)
admin.site.register(User_Mahou_Shoujo, UserMahouShoujoAdmin)
