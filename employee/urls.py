from django.urls import path
from . import views as v
urlpatterns=[
    path('',v.base,name="homepage"),
    path('login',v.logins,name="loginpage"),
    path('add',v.add,name="addemp"),
    path('mng',v.manage,name="mnemp"),
    path('edit_employee<str:emp_id>',v.edit,name="edit"),
    path('delete_employee<str:emp_id>',v.delete,name="delete"),
    path('logout', v.logouts,name="logout"),
]