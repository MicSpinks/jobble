from django.shortcuts import render
from django.db import models
from django.contrib.auth import get_user_model
from jobs.models import JobPosting
from django.db.models import Q

User = get_user_model()

def index(request):
    candidates = None

    if request.user.is_authenticated and getattr(request.user, "role", None) == "recruiter":
        # Get all jobs posted by this recruiter
        recruiter_jobs = JobPosting.objects.filter(posted_by=request.user)

        # Collect all required skills from their jobs
        job_skills = []
        for job in recruiter_jobs:
            if job.skills:
                job_skills.extend([s.strip() for s in job.skills.split(",") if s.strip()])

        # If recruiter has jobs with skills, find matching candidates
        if job_skills:
            q = Q()
            for skill in job_skills:
                q |= Q(skills__icontains=skill)

            candidates = (
                User.objects.filter(role="user")
                .filter(q)
                .order_by("-date_joined")[:6]
            )

    return render(request, "Rhome/index.html", {
        "candidates": candidates,
    })
def postjobs(request):
 return render(request, 'Rhome/postjobs.html')

def searchcandidates(request):
	from django.contrib.auth import get_user_model
	User = get_user_model()
	query = request.GET.get('q', '').strip()
	candidates = User.objects.filter(role='user')
	if query:
		# simple search across username, headline, skills, location
		candidates = candidates.filter(
			models.Q(username__icontains=query) |
			models.Q(headline__icontains=query) |
			models.Q(skills__icontains=query) |
			models.Q(location__icontains=query)
		)
	# pass candidates to template
	return render(request, 'Rhome/searchcandidates.html', {'candidates': candidates, 'query': query})

def organizeapplicants(request):
 return render(request, 'Rhome/organizeapplicants.html')

def messages(request):
	return render(request, 'Rhome/messages.html')