from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
# from  django.shortcuts import Http404
from .models  import Choice,Question
from  django.http import  HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic



class  IndexView(generic.ListView):
    template_name  = "polls/index.html"
    context_object_name  =  "latest_question_list"
    
    def  get_queryset(self):
        """Return the last five published  questions"""
        return Question.objects.order_by("-pub_date")[:5]
    
 
 



class  DetailView(generic.DetailView):
    model =  Question
    template_name  = "polls/detail.html"
     

class  ResultsView(generic.DetailView):
    model = Question
    template_name  =  "polls/detail.html"
   
   

class  vote(generic.DetailView):
    model  =  Question
    template_name  = "polls/results.html"
       

