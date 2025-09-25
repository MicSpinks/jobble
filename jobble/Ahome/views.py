from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'Ahome/index.html')

def manageposts(request):
    return render(request, 'Ahome/manageposts.html')

def manageusers(request):
    return render(request, 'Ahome/manageusers.html')
