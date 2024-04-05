from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Departments, Doctors

from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    
    if request.method=='POST':
        
        form = BookingForm(request.POST)
        if form.is_valid():
            print('valid form')                       
            form.save()
            form = BookingForm()
            
            # return render(request, 'confirmation.html')
            return redirect('success')

    else:    
        form = BookingForm()

        dict_form = {
            'form': form
        }
    print('Not valid')
    return render(request, 'booking.html', dict_form)

##########################################

def success(request):
    return render(request, 'success.html')


##########################################



def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept = {
        'dept': Departments.objects.all(),
    }
    return render(request, 'department.html', dict_dept)