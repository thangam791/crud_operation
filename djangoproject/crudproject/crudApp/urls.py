from django.urls import path
from .views import *


urlpatterns=[
     path(r'employee_api/',emp_view),
     path(r'create_employee/',emp_create),
     path(r'update_employee/<int:id>',emp_update),
     path(r'delete_employee/<int:id>',emp_delete),
]