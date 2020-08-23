from django.http import Http404
from django.shortcuts import render
from .models import Question,Choice
# Create your views here.
def polls(request):
    poll=Question.objects.order_by('-pub_date')[:5]
    
    context = {
        'poll': poll,
    }
    return render(request,'index.html',context)

def details(request,id):
    try:
        question=Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404('question is not exist')
    return render(request,'details.html',{'question':question})
def result(request,question_id):
    return HttpResponse('this is results %s'%question_id)
def votes(request,question_id):
    return HttpResponse('this is votes %s'%question_id)