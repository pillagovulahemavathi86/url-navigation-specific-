from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request,'python.html')

def details(request):
    return render(request,'details.html')
