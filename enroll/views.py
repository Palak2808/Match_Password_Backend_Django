from django.shortcuts import render
from .forms import StudentRegisteration #from forms file import the class which created the form.
# from enroll.models import Student
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm=StudentRegisteration(request.POST)
        if fm.is_valid():
            print('FORM VALIDATED')
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
            print('Password:',fm.cleaned_data['pas'])
            print('Confirm Password:',fm.cleaned_data['pas2'])
            

    else:
        fm=StudentRegisteration()
    
    return render(request,'enroll/userregisteration.html',{'form':fm})
    
    

 