from django.shortcuts import render,HttpResponse,redirect
from .models import User,Employee

# Create your views here.
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def base(request):
    return render(request,"base.html")

def logins(request):
    if request.method == 'POST':
        usename=request.POST.get('usname')
        pswdd=request.POST.get("pas1")
        user=authenticate(request,username=usename,password=pswdd)
        if user is not None and user.is_staff == 1:
            login(request,user)
            return render(request,'admin.html') 
        elif user is not None and user.usertype =="employee":
            login(request,user)
            return render(request,"employee.html")
        else:
            return redirect(logins)
           
    else:
        return render(request,'login.html')

@login_required
def logouts(request):
    logout(request)
    return redirect(logins)


@login_required
def add(request):
    if request.method == 'POST':
        usname=request.POST.get('mail')
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("mail")
        password=request.POST.get("pasd")
        address=request.POST.get("adrs")
        phone=request.POST.get("phn")
        ustype="employee"
        k=User.objects.create_user(first_name=fname,last_name=lname,email=email,password=password,username=usname,usertype=ustype)
        emp=Employee()
        im=request.FILES['photo']
        emp.image=im
        emp.phone=phone
        emp.address=address
        emp.us_id=k.id
        emp.save()
        messages.success(request,"successfully added employee!")
        return render(request,"add.html")
    else:
        return render(request,'add.html')
        messages.error(request,"failed to add employee!")


@login_required
def manage(request):
    empl=Employee.objects.all()
    return render(request,"manage.html",{"empl":empl})


@login_required
def edit(request,emp_id):
    if request.method == "GET":
        employee=Employee.objects.get(us_id=emp_id)
        return render(request,"edit.html",{"employee":employee})
    else:
        p=User.objects.get(id=emp_id)
        p.first_name=request.POST.get('fname')
        p.last_name=request.POST.get('lname')
        p.email=request.POST.get('mail')
        p.username=request.POST.get('mail')
        p.save()

        e1=Employee.objects.get(us_id=emp_id)
        e1.address=request.POST.get('adrs')
        e1.user_id=p.id
        e1.save()
        return render(request,"edit.html",{ 'success':'Successfully edited employee!' })

@login_required
def delete(request,emp_id):
    dele=Employee.objects.get(us_id=emp_id)
    dl=User.objects.get(id=emp_id)
    dele.delete()
    dl.delete()
    return redirect(manage)


