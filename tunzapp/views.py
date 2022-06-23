
from multiprocessing import context
import re
from django.shortcuts import render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from .models import *
from .models import Child,Donor

# Create your views here.
#View function for home: To be done by Julia
def home(request):
    '''view for home'''
    return render(request, 'tunzapp/home.html')


#view function for registration: Done by Andre/Oliver
def signup(request):
    '''view for signup'''
    form = CreateUserForm()
    
        
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
            
    context ={
        'form': form,
        }        
    
    return render(request,'accounts/register.html', context)


#view function for login_page:Done by Andre/Oliver
def login_page(request):
    '''view for login'''
    
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        print(username,password,user)
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.info(request, 'Check username or password !')
        
    return render(request, 'accounts/login.html')   


#view function for about section:To be done by Oliver
def about(request):
    
    return render(request, 'tunzapp/about.html')

#view function for specific details for the child:Ludwig
def details(request, pk):
    child = Child.objects.get(id=pk)
    child_data = Child.objects.filter(id=pk)
    if request.method == 'POST':
        the_child = child
        amount = request.POST.get('amount')
        donated_by = request.user
        
        donation = Donor.objects.create(child=the_child, amount=amount, donated_by = donated_by)
    
    transactions = Donor.objects.filter(id=pk)
    
    # financial = FinancialNeed.objects.filter()
    context= {
        'child':child,
        'child_data':child_data,
        'transactions': transactions
        
        }
    print(child)
    return render(request, 'tunzapp/details.html',context)

#view function for the list of children :To be done by Nimrod
def list(request):
    return render(request, 'tunzapp/list.html')
     

#view function for logout_user:Done by Andre/Oliver
def logout_user(request):
    '''logout user'''
    logout(request)
    return redirect('login')