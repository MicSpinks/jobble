from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from jobs.models import JobPosting
from .forms import ApplicationForm
from .models import Application, JobPosting
from django.http import JsonResponse

STATUS_ORDER = {
    'AP': 0,
    'RV': 1,
    'IV': 2,
    'OF': 3,
    'CL': 4,
}


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
            application.status = Application.APPLIED
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

@login_required
def withdraw_application(request, pk):
    app = get_object_or_404(Application, pk=pk, applicant=request.user)
    if request.method == "POST":
        app.delete()
    return redirect('applications:my_applications')

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
    
    # Sort applications by job and status
    applications = sorted(
        applications,
        key=lambda app: (app.job.id, STATUS_ORDER.get(app.status, 99))
    )

    return render(request, 'applications/recruiter_applicants.html', {'applications': applications})

@login_required
def update_status(request, application_id):
    application = get_object_or_404(Application, id=application_id)

    new_status = request.POST.get('status')
    valid_statuses = dict(Application.STATUS_CHOICES)

    if new_status in valid_statuses:
        application.status = new_status
        application.save()
        return JsonResponse({
            'success': True,
            'new_status': new_status,
            'label': valid_statuses[new_status]
        })
    else:
        return JsonResponse({'error': 'Invalid status'}, status=400)