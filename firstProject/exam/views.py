from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
# Create your views here.

@csrf_protect
def testPaper(request):

    #business Logic
    que="What is the product of 3 and 4?"
    option_a="7"
    option_b="12"
    option_c="16"
    option_d="21"
    answer="12"

    d={'question': que,
       'options':[option_a, option_b, option_c, option_d],
       'answer':answer,
        }
    res=render(request,'exam/test_paper.html',d)
    return res

def result(request):
    s="<h1>Please Submit the Test first</h1>"
    if request.method=="POST":
        v=request.POST['option']
        if v==str(request.POST['answer']):
            s="Congratulations! Your answer is correct"
        else:
            s="Sorry! Your Answer is not Correct"
    return HttpResponse(s)