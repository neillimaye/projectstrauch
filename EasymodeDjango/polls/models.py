from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
# Store the blueprint for any abstract 'object' in your django app

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self): #custom function
           #return self.pub_date >= timezone.now() - datetime.timedelta(days=1)  #just checks if it's more than a day old
            now = timezone.now()
            return now - datetime.timedelta(days=1) <= self.pub_date <= now #filters out anything published from the future
            was_published_recently.admin_order_field = 'pub_date' #when sorting by whether something was published recently
                                                                  #in the admin view, sort by its publication date instead
            was_published_recently.boolean = True # have it display a red X or a green checkmark in the any list view
            was_published_recently.short_description = 'Published recently?' # Replaces "Was Published Recently" as the header in any list view

#blueprints for the question being asked and what a 'choice' looks like
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #manually configuring the fact that choices 'belong' to a question
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
        #overwrites the Model __str__ function to return a string representation of the data



'''
What each part means
[we're making a class] [name of our class]([subclasses, or inherits, the django Model library]):
    various properties, note that they all use data types from the models library
    in addition, properties like max_length and default set limits and original values upon creation of a new object
    these are effectively constructors for any abstract 'thing' that will be used in this app
'''
