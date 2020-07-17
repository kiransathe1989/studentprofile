from django.shortcuts import render,redirect
from App1.models import Employeemodel
from django.db import IntegrityError

# Create your views here.
def showindex(request):
    return render(request,'hone.html')


def login(request):
    return render(request,"studentlogin.html")


def register(request):
    return render(request,"Rgistration.html")
def savedata(request):
    emp_name = request.POST["Ename"]
    emp_age = request.POST["EAge"]
    emp_gen = request.POST["a1"]
    emp_con = request.POST["Econ"]
    emp_emil = request.POST["Email"]
    emp_euser = request.POST["EUser"]
    emp_epssw = request.POST["Epssw"]
    chekUser=Employeemodel.objects.values('Username')

    print(chekUser)
    if {'Username':emp_euser} in chekUser:
        return render(request, "Rgistration.html", {"data1":'User with this username already exists'})
    else:
        Employee_information = Employeemodel(Name=emp_name, Age=emp_age, Contact=emp_con, Username=emp_euser,Email=emp_emil, Password=emp_epssw, gender=emp_gen)
        Employee_information.save()
        return render(request, "Rgistration.html", {"data1": 'Register succefully'})


def savestudent(request):
        user_name = request.POST.get("Username")
        user_passw = request.POST.get("t2")

        try:
            Employeemodel.objects.get(Username=user_name,Password=user_passw)
            studentdata= Employeemodel.objects.filter(Username=user_name)
            return render(request, "studentwelcome.html",{"data":studentdata})
        except Employeemodel.DoesNotExist:
            return render(request, "studentlogin.html", {"data": 'Please Enter valid User name and Password'})


def forgotpassw(request):
    return render(request,"forgotpassw.html")


def newpassword(request):
    user_name = request.POST.get("t")
    new_passw=request.POST.get("t1")
    conform_new=request.POST.get("t2")
    chek = Employeemodel.objects.values('Username')
    if {'Username': user_name} in chek:
        if new_passw == conform_new:
            res = Employeemodel.objects.filter(Username=user_name)
            res.update(Name=user_name,Password=conform_new)
            return render(request,"studentwelcome.html",{"data1":'Password change succefully'})
        else:
            return render(request,"studentwelcome.html",{"data1":'New passowrd & conform password should be same'})
    else:
        return render(request,"studentwelcome.html", {"data1": 'User name dosnot exit'})


def admin(request):
   # all_Employee=Employeemodel.objects.all()
    return render(request,"Admin.html")


def create(request):
    return render(request,"ceate.html")


def veiws(request):
    All_Emp=Employeemodel.objects.all()
    return render(request,"veiw.html", {"data6":All_Emp})


def updete(request):
    All_Emp = Employeemodel.objects.all()
    return render(request,"updete.html", {"data7":All_Emp})


def update_Emp(request):
    updet=request.GET.get("mno")
    print(updet)
    apdete= Employeemodel.objects.filter(Username=updet)
    return render(request,"update_Emp.html",{"data8":apdete})


def update2_Emp(request):
    updet = request.GET.get("mno")
    res2 = Employeemodel.objects.filter(Username=updet)
    print(res2)
    return render(request,"update_Emp.html",{'data12':res2})




def delete(request):
    delete=Employeemodel.objects.all()
    return render(request,"delete.html",{'dada13':delete})


def delet2_Emp(request):
    det=request.GET['mno']
    Employeemodel.objects.filter(Username=det).delete()
    d="Employee Deleted"
    return render(request,"delete.html",{'data14':d})


def save(request):
    name=request.POST.get("t1")
    age=request.POST.get("t2")
    Contact=request.POST.get("t3")
    Email=request.POST.get("t4")
    Username=request.POST.get("t5")
    Password=request.POST.get("t6")
    gender=request.POST.get("t7")
    updet=Employeemodel.objects.get(Username=Username)
    updet.Name=name
    updet.Age=age
    updet.Contact=Contact
    updet.Email=Email
    #updet.Username=name
    updet.Password=Password

    updet.gender=gender
    updet.save()
    return render(request,"save.html")