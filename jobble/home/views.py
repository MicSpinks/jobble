from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import JobPosting
from django.db.models import Q

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
    titlequery = request.GET.get("titlequery")
    locationquery = request.GET.get("locationquery")
    skillsquery = request.GET.get("skillsquery")
    remote = request.GET.get("remote")
    visa = request.GET.get("visa")
    minsalary = request.GET.get("minsalary")
    maxsalary = request.GET.get("maxsalary")
    jobs = JobPosting.objects.all().order_by('-date_posted')
    
    if titlequery:
        jobs = jobs.filter(title__icontains=titlequery)
    if locationquery:
        jobs = jobs.filter(location__icontains=locationquery)
    if skillsquery:
        skill_list = [s.strip() for s in skillsquery.split(",") if s.strip()]
        q = Q()
        for skill in skill_list:
            q |= Q(skills__icontains=skill)
        jobs = jobs.filter(q)
    if remote:
        jobs = jobs.filter(remote_or_onsite__icontains=remote)
    if visa:
        jobs = jobs.filter(visa_sponsorship__icontains=visa)
    if minsalary:
        jobs = jobs.filter(min_salary__gte=int(minsalary))
    if maxsalary:
        jobs = jobs.filter(max_salary__lte=int(maxsalary))

    return render(request, 'home/jobs.html', {'jobs': jobs})

def maps(request):
 return render(request, 'home/maps.html')

