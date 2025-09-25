from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPosting
from .forms import JobPostingForm  # assuming you already made a ModelForm

@login_required
def edit_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)

    # Only allow the original poster
    if job.posted_by != request.user:
        raise PermissionDenied

    if request.method == "POST":
        form = JobPostingForm(request.POST, instance=job)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostingForm(instance=job)

    return render(request, "jobs/edit_job.html", {"form": form, "job": job})



def job_list(request):
    jobs = JobPosting.objects.all().order_by('-date_posted')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def create_job(request):
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user   # save recruiter
            job.save()
            return redirect('job_list')
    else:
        form = JobPostingForm()
    return render(request, 'jobs/create_job.html', {'form': form})