from django.shortcuts import render, get_object_or_404, redirect
from jobs.models import JobPosting
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from jobs.models import JobPosting  

# Create your views here.

def index(request):
    template_data = {'title': 'Jobble'}
    user = request.user
    jobs = JobPosting.objects.all().order_by('-date_posted')

    # Auto-filter based on user’s skills if logged in
    if user.is_authenticated and hasattr(user, "skills") and user.skills:
        skill_list = [s.strip() for s in user.skills.split(",") if s.strip()]
        q = Q()
        for skill in skill_list:
            q |= Q(skills__icontains=skill)
        jobs = jobs.filter(q)

    jobs = jobs[:6]  # limit results for homepage

    return render(request, 'home/index.html', {
        'template_data': template_data,
        'jobs': jobs,
    })

def applications(request):
 return render(request, 'home/applications.html')

# Renders the jobs page while filtering results based on user input
def jobs(request):
    user = request.user
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
    if skillsquery == "true" and user.is_authenticated:
        skill_list = [s.strip() for s in user.skills.split(",") if s.strip()]  # split the text field into list
        q = Q()
        for skill in skill_list:
            q |= Q(skills__icontains=skill)  # assuming JobPosting.skills is also a text field
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

@login_required
def messages(request):
    return render(request, 'home/messages.html')

