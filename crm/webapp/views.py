from django.shortcuts import render,redirect
from .forms import CreationUserForm, LoginForm,CreateRecordForm, UpdateRecordForm
from .models import Record

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from django.contrib import messages





def home(request):
    return render(request, 'webapp/index.html')


# Register

def register(request):
    form = CreationUserForm()
    if request.method == "POST":
        form = CreationUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        
    context = {
        'form' : form
    }
    return render(request, 'webapp/register.html', context)

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("/dashboard/")
            
    context = {'form': form}

    return render(request, 'webapp/login.html', context=context)

# Logout
def logout(request):
    auth.logout(request)

    messages.success(request, "Logout success!")
    return redirect("/login/")




# dashbaord
@login_required(login_url='login')
def dashboard(request):
    records= Record.objects.all()

    context = {'records' : records,}
    return render(request, "webapp/dashboard.html", context=context)


# craete record
@login_required(login_url='login')
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Data is created!!")
            return redirect("/dashboard/")
        
    context = {
        "form": form    }
    
    return render(request, 'webapp/create_record.html', context)
        
# Update record
@login_required(login_url='login')
def update_record(request, pk):

    record = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Updated!!")
            return redirect("/dashboard/")
    context = {
        'form' : form
    }
    return render(request, 'webapp/update_record.html', context)

# view singular data
@login_required(login_url='login')
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {
        'record': record
    }

    return render(request, 'webapp/view_record.html', context)

@login_required(login_url='login')
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Data Delete Sucessfylly!!')
    return redirect('/dashboard/')

            