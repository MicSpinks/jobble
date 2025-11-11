from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, get_object_or_404, redirect
from .models import JobPosting
from .forms import JobPostingForm  # assuming you already made a ModelForm
from jobble.utils import geocode_location


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


from applications.forms import ApplicationForm

def job_list(request):
    jobs = JobPosting.objects.all().order_by('-date_posted')
    form = ApplicationForm()  # blank form for the modal
    return render(request, 'jobs/job_list.html', {'jobs': jobs, 'form': form})

@login_required
def create_job(request):
    # Ensure only recruiters can create jobs
    if request.user.role != 'recruiter':
        return redirect('home')
    
    if request.method == 'POST':
        form = JobPostingForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.posted_by = request.user
            
            # Geocode the location
            location = form.cleaned_data.get('location')
            if location:
                geo_data = geocode_location(location)
                if geo_data:
                    job.latitude = geo_data['latitude']
                    job.longitude = geo_data['longitude']
                    job.city = geo_data['city']
                    job.state = geo_data['state']
                    job.country = geo_data['country']
            
            job.save()
            return redirect('job_list')  # Or wherever you want to redirect
    else:
        form = JobPostingForm()
    
    return render(request, 'jobs/create_job.html', {'form': form})