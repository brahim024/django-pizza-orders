from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404,render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from .models import Question,Choice

# Create your views here.

'''class PollView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name='latest_question_list'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]'''
        

def polls(request):
    poll=Question.objects.order_by('-pub_date')[:5]
    
    context={
        'poll': poll,
    }
    return render(request,'polls/index.html',context)

def details(request,id):
    try:
        question=Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404('question is not exist')
    return render(request,'polls/details.html',{'question':question})

def result(request,id):
    question =get_object_or_404(Question,pk=id)
    return render(request,'polls/result.html',{'question':question})
def votes(request,id):
    question=get_object_or_404(Question,pk=id)
    try:
        selected=question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render (request,'polls/details.html',{
            'question':question,
            'error_message':'please select any choices',
        })
    else:
        selected.votes +=1
        selected.save()
    
        return HttpResponseRedirect (reverse('polls:result',args=(question.id,)))
    
    