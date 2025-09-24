from django.shortcuts import render

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Jobble'
    return render(request, 'home/index.html', {
    'template_data': template_data})

def applications(request):
 return render(request, 'home/applications.html')

def jobs(request):
 return render(request, 'home/jobs.html')

def maps(request):
 return render(request, 'home/maps.html')