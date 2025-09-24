from django.shortcuts import render

# Create your views here.
def index(request):
 return render(request, 'Rhome/index.html')

def postjobs(request):
 return render(request, 'Rhome/postjobs.html')

def searchcandidates(request):
 return render(request, 'Rhome/searchcandidates.html')

def organizeapplicants(request):
 return render(request, 'Rhome/organizeapplicants.html')