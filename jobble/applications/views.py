from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import JobPosting
from .forms import ApplicationForm

@login_required
def apply_to_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)

    if Application.objects.filter(job=job, applicant=request.user).exists():
        return redirect('applications:my_applications')

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.applicant = request.user
            application.save()
            return redirect('applications:my_applications')
    else:
        form = ApplicationForm()

    return render(request, 'applications/apply_modal.html', {'form': form, 'job': job})

@login_required
def my_applications(request):
    applications = Application.objects.filter(applicant=request.user)
    return render(request, 'applications/my_applications.html', {'applications': applications})

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Application, JobPosting

@login_required
def recruiter_applicants(request):
    user = request.user
    # Ensure the user is a recruiter
    if user.role != 'recruiter':
        return render(request, 'applications/not_authorized.html')

    # Get all jobs posted by this recruiter
    jobs = JobPosting.objects.filter(posted_by=user)

    # Get all applications for those jobs
    applications = Application.objects.filter(job__in=jobs).select_related('job', 'applicant')

    return render(request, 'applications/recruiter_applicants.html', {'applications': applications})

