from django.urls import path
from task import views


urlpatterns = [ 
    path('', views.login, name='login'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('employee_experience',views.employee_experience,name='experience'),
    path('employee_experience/<int:employee_id>/',views.employee_experience,name='experience'),
    path('logout',views.logout,name='logout'),
    path('save_employee_experience/', views.save_employee_experience, name='save_employee_experience'),

]