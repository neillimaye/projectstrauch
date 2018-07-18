from django.urls import path

from . import views

app_name = 'polls' #so that views can specify that they're for the polls app
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'), #turns anything without any text after the web address into a request to see the 'index' view, i.e. that which is defined in views.py
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),  #turns anything with /polls/[a number, referencing the question id]/)
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'), # etc
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'), # etc
]
