from django.db import models
#importing models from django to be used in our enviroments
import datetime
from django.utils import timezone


class Question(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days=1)
    




class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    # this code creates a relationship where
    # each instance of the current model is associated with a single Question instance
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #this line of code defines an integer field
    # named "votes" in the current Django model.
    
    


