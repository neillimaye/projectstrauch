from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# views.py is made to render the pages within the polls app

# Create your views here.

from .models import Choice, Question #need this to use the Question functions, like getting all instances of the objects (not defined in models.py, but in Django's model.py library)

def index(request):
    #by the way, this 'request' parameter refers to whatever session is going on between the server and the client, AFAICT
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html') #get the template from index.html
    context = {
        'latest_question_list': latest_question_list, #context = dictionary that maps variable names to python opjects ('latest_question_list' to the variable latest_question_list defined above)
    } #note that this is where latest_question_list is defined, and index.html only refers to this variable
    # return HttpResponse(template.render(context, request))
    return render(request, 'polls/index.html', context) #shorthand for the above line



#in polls/urls.py, url patterns are defined (like '' or '[some number]/vote') and mapped to these functions
def detail(request, question_id):
    # There are two ways to do this, i.e. there are two ways to load question details using the id parameter for reference
    #
    # try:
    #     question = Question.objects.get(pk=question_id);
    # except Question.DoesNotExist: #catch this specific exception
    #     raise Http404("Question does not exist")
    # return render(request, 'polls/detail.html', {'question':question});
    # Argument by argument - render, using this current session info, the detail.html view found in /polls/, and mapping the 'question' in the html file to question in this file
    #original placeholder render- return HttpResponse("You're looking at question %s." % question_id)

    # then, there's the shorthand way suing the get_object_or_404 library from django.shortcuts
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})
    #this return statement is the same as above, use the commented block above for detail

def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    # above - former dummy code. below - useful functioning code
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

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
