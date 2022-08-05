from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from testapp.models import Employee,testapp_user
from django.contrib.auth import authenticate,login,logout


# Create your views here.
@csrf_protect
def greeting(request):
    res=render(request,'testapp/greeting.html')

    return res

def about(request):
    res=render(request,'testapp/about.html')
    return res

def showContact(request):
    res=render(request,'testapp/show_contact.html')
    return res

def employee_info(request):
    if 'username' not in request.session:
        return HttpResponseRedirect("http://localhost:8000/testapp/login")
    employees=Employee.objects.all()
    data={
        'employees': employees,
    }
    res=render(request,'testapp/show_employee.html', data)
    return res

def newEmployee(request):
    res=render(request,'testapp/new_employee.html')
    return res

def saveEmployee(request):
    if request.method=='POST':
        formData=request.POST
        emp=Employee()
        emp.eno=formData['eno']
        emp.ename=formData['ename']
        emp.esal=formData['esal']
        emp.eprofile=formData['eprofile']
        emp.save()
    s="http://localhost:8000/testapp/show-employee"
    return HttpResponseRedirect(s)

def userLogin(request):
    data={}
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username, password=password)
        if user:
            login(request,user)
            request.session['username']=username
            return HttpResponseRedirect("http://localhost:8000/testapp/show-employee")
        else:
            data['error']="Username or Password is incorrect"
            return render(request, 'testapp/user_login.html', data)
    else:
        return render(request,'testapp/user_login.html', data)

def userlogout(request):
    logout(request)
    return HttpResponseRedirect("http://localhost:8000/testapp/login")

