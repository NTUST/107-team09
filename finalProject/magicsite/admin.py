from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Question_Set)
admin.site.register(Question)
admin.site.register(Option)