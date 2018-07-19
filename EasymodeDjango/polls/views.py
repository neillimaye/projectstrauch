from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    # override the context variable from the default '<model name>_list'
    # that way we don't have to update that part in the templates

    def get_queryset(self):
        # """Return the last five published questions."""
        # return Question.objects.order_by('-pub_date')[:5]
        # above was the old way of doing it in the Django tutorial
        return Question.objects.filter(
        pub_date__lte=timezone.now()    #written onto multiple lines for ease of reading
        ).order_by('-pub_date')[:5]     #unlike my comments
        


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

'''
generic.ListView and generic.DetailView are generic views that 'display a list of objects'
and 'display details for a particular type of object'

model - what the view is acting upon

DetailView uses the '<app name>/<model name>_detail.html' convention for finding its templates
we hard-code specify template_name just in case it gets something wrong
we do it for both results and details because those views render different sets of information

Most of the stuff written here under the class names overrides the default variable names
that are defined in the generic library

'''
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id) - again, was used for the dummy implementation
    question = get_object_or_404(Question, pk=question_id) #first see if we can get the question
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # try to get the choice selected by the user
        # request.POST is a local data set of all the data submitted through  the HTTP POST method
        # Returns the ID of the data with the keyname 'choice'
    except (KeyError, Choice.DoesNotExist):
        # checks for KeyError, i.e. the key 'choice' does not exist, which we've prevented in the detail.html template
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # in all other cases, do this
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
        # reverse is similar to url functionality
        # it will call the 'results' view with the current question ID
        # that is, once the voting is done, the results page is shown
