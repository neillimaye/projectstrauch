from django.contrib import admin

# Register your models here.
# i.e. tell Django that there is an admin interface for certain models

from .models import Question, Choice
# the . is from file navigation language. it means 'start in the directory i'm currently in'
# since this is in the polls directory, and we need to import from the Question.py under models/
# we need to use the . operator

class ChoiceInLine(admin.TabularInline): #create a blueprint for how we have inline listed things using the StackedInline library under the Django admin library
                        # TabularInLine puts it in a more horizontal-oriented format
                        # while StackedInline puts each element vertically
                        # play around with these two display options to get the gist of why TabularInLine is used, it's more space efficient
    # We could use admin.site.register(Choice) to get a default form
    model = Choice # what model we're using in this admin edit view
    extra = 3 # how much space for extra stuff it can have

class QuestionAdmin(admin.ModelAdmin): #note that all these variables override the default, empty, variables that define the default list view
    # Two ways to do this - with fields and fieldsets
    # fields = ['pub_date','question_text'] #control what fields are there
    # note that this makes the edit form display changing the pub date parameter before the q text

    list_display = ('question_text', 'pub_date', 'was_published_recently') #override the default listing
                    #this sets it to show the question text, the publishing date, and whether it was published recently
    list_filter = ['pub_date'] # adds a filter option on the right hand side like when you're shopping on Amazon
                               # Django sees 'pub_date' and knows it's dealing with an objected related to dates
                               # so in this case, it automatically includes option to filter out by
                               # 'Any Date', 'Today', 'Past 7 days', 'This Month', 'This Year'
    search_fields = ['question_text'] # Adds a search bar that sorts by the 'question_text' component

    fieldsets = [ #fieldsets modifies what all can be edited
        (None,               {'fields': ['question_text']}), #(Text over the box, what information you can edit in that box)
        ('Date information', {'fields': ['pub_date']}),
    ] #this is a fancier way that directly changes what the actual admin form looks like


    inlines = [ChoiceInLine]
admin.site.register(Question, QuestionAdmin) #actually registers the thing, creates a default form
# the QuestionAdmin parameter is there to customize the look and feel of the form
