# Create your views here.
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Employee, Experience
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request, "base.html")



def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            employee = Employee(name=name, email=email, phone=phone, password=password)
            employee.save()
            return redirect('login')
        else:
            return render(request, 'register.html', {'error': 'Passwords do not match'})
    else:
        return render(request, 'register.html')

session=dict()
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        employee = Employee.objects.filter(email=email, password=password).first()
        if employee:
            global session
            user = Employee.objects.get(id=employee.id)
            session["employee"]=user.employee_id
            print(session,user.employee_id)
            return redirect(reverse('experience',kwargs={'employee_id': user.employee_id}))
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'login.html')
    
def employee_experience(request,employee_id=0):
    try:
        global session
        print(session,employee_id)
        if session:
            experiences= Experience.objects.filter(employee=employee_id)
            if request.method == 'POST':
                return render(request, 'employee_experience.html', {'experiences': experiences,'employee_id':employee_id})
            elif (request.method == 'GET'):
                return render(request, 'employee_experience.html', {'experiences': experiences,'employee_id':employee_id})
        else:
            session.clear()
            return redirect('login')
    except:
            session.clear()
            return redirect('login')
  
def logout(request):
    if request.method == 'POST':
        global session
        if session:
            session.clear()
            return redirect('login')
        else:
            experiences = Experience.objects.filter(employee_id=session['employee'])
            return render(request, 'employee_experience.html', {'experiences': experiences})
    else:
        return render(request, "base.html")

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

def save_employee_experience(request):
    global session
    print(session)
    if request.method == 'POST':
        experience_counter = request.POST.get('experience_counter')
        print(experience_counter)
        for i in range(1,int(experience_counter)+1):
            company_names = request.POST.get('company_name_'+str(i))
            roles = request.POST.get('role_'+str(i))
            dates_of_joining = request.POST.get('date_of_joining_'+str(i))
            last_dates = request.POST.get('last_date_'+str(i))
            print("Company Name:", company_names)
            print("Role:", roles)
            print("Date of Joining:", dates_of_joining)
            print("Last Date:", last_dates)
            print("--------------------------------")
            employee_instance = get_object_or_404(Employee, employee_id=session['employee'])
            experience_db = Experience(company_name=company_names,role_name=roles, date_of_joining=dates_of_joining, last_date=last_dates, employee=employee_instance)
            experience_db.save()
        return JsonResponse({'message': 'Employee experience saved successfully.'})
    else:
        return JsonResponse({'error': 'Invalid request method.'})
