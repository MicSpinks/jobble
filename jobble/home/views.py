from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import JobPosting

# Create your views here.
def index(request):
    template_data = {}
    template_data['title'] = 'Jobble'
    return render(request, 'home/index.html', {
    'template_data': template_data})

def applications(request):
 return render(request, 'home/applications.html')

# Renders the jobs page while filtering results based on user input
def jobs(request):
    query = request.GET.get("q")
    jobs = JobPosting.objects.all().order_by('-date_posted')
    
    if query:
        jobs = jobs.filter(title__icontains=query)

    return render(request, 'home/jobs.html', {'jobs': jobs})

def maps(request):
 return render(request, 'home/maps.html')

