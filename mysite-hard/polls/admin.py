from django.contrib import admin

# Register your models here.
# i.e. tell Django that there is an admin interface for certain models

from .models import Question
# the . is from file navigation language. it means 'start in the directory i'm currently in'
# since this is in the polls directory, and we need to import from the Question.py under models/
# we need to use the . operator
admin.site.register(Question) #actually registers the thing
