from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from django.contrib.auth import get_user_model
from jobs.models import JobPosting
from django.db.models import Q
from .models import SavedSearch


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
    User = get_user_model()
    query = request.GET.get('q', '').strip()
    save_search_name = request.GET.get('save_search', '').strip()
    action = request.GET.get('action', '').strip()

    candidates = User.objects.filter(role='user')

    # perform the search
    if query:
        candidates = candidates.filter(
            models.Q(username__icontains=query) |
            models.Q(headline__icontains=query) |
            models.Q(skills__icontains=query) |
            models.Q(location__icontains=query)
        )

    if action == "save" and query:
        if save_search_name:
            SavedSearch.objects.create(
                user=request.user,
                name=save_search_name,
                query=query
            )
        else:
            SavedSearch.objects.create(
                user=request.user,
                name=query,
                query=query
            )

    # always load this user's saved searches
    saved_searches = SavedSearch.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'Rhome/searchcandidates.html', {
        'candidates': candidates,
        'query': query,
        'saved_searches': saved_searches,
    })

def delete_saved_search(request, search_id):
    """Delete a saved search belonging to the current user."""
    saved_search = get_object_or_404(SavedSearch, id=search_id, user=request.user)
    saved_search.delete()
    return redirect('Rhome.searchcandidates')

def organizeapplicants(request):
 return render(request, 'Rhome/organizeapplicants.html')

def messages(request):
	return render(request, 'Rhome/messages.html')