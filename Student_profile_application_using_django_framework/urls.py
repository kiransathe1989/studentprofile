"""Student_profile_application_using_django_framework URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from App1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showindex ,name="home"),
    path('login/',views.login,name="login"),
    path('studentlogin/',views.savestudent,name="studentlogin"),
    path('register/',views.register,name="register"),
    path('savedata/',views.savedata,name="savedata"),
    path('forgotpassw/',views.forgotpassw,name="forgotpassw"),
    path('Newpassword/',views.newpassword,name="Newpassword"),
    path("Admin/",views.admin,name="Admin"),
    path('create/',views.create,name="create"),
    path('veiw/',views.veiws,name="veiw"),
    path('updete/',views.updete,name="updete"),
    path('update_Emp/',views.update_Emp,name="update_Emp"),
    path('update2_Emp/',views.update2_Emp,name='update2_Emp'),
    path('delete/',views.delete,name="delete"),
    path('delet2_Emp/',views.delet2_Emp,name="delet2_Emp"),
    path('save/',views.save,name="save")
]