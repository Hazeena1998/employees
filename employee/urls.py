from django.urls import path
from . import views as v
urlpatterns=[
    path('',v.home,name="homepage"),
    path('about',v.about,name="aboutpage"),
    path('contact',v.contact,name="contactpage"),
    path('login',v.logins,name="loginpage"),
    path('logout',v.logouts,name="logoutpage"),
    path('add',v.add,name="addemp"),
    path('mng',v.manage,name="mnemp"),
    path('edit_employee<str:emp_id>',v.edit,name="edit"),
    path('delete_employee<str:emp_id>',v.delete,name="delete"),
]