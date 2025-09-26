from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from jobs.models import JobPosting
from accounts.models import CustomUser

# Create your views here.
def index(request):
    return render(request, 'Ahome/index.html')

def manageposts(request):
    jobs = JobPosting.objects.all().order_by('-date_posted')
    return render(request, 'Ahome/manageposts.html', {'jobs': jobs})

def manageusers(request): 
    users = CustomUser.objects.all().order_by('-date_joined')
    return render(request, 'Ahome/manageusers.html', {'users': users})

@login_required
def delete_job(request, job_id):
    job = get_object_or_404(JobPosting, id=job_id)

    if request.user.is_superuser == False:
        messages.error(request, "You are not allowed to delete this job.")
        return redirect("job_list") 

    if request.method == "POST":
        job.delete()
        messages.success(request, "Job deleted successfully.")
        return redirect("Ahome.manageposts")

    return redirect("Ahome.manageposts")

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id = user_id)

    if request.user.is_superuser == False:
        messages.error(request, "You are not allowed to delete this job.")
        return redirect("job_list") 

    if request.method == "POST":
        user.delete()
        messages.success(request, "User deleted successfully.")
        return redirect("Ahome.manageusers")

    return redirect("Ahome.manageusers")

@user_passes_test(lambda u: u.is_superuser)
def change_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == "POST":
        new_role = request.POST.get("role")
        if new_role in dict(CustomUser.ROLE_CHOICES):
            user.role = new_role
            user.save()
            messages.success(request, "Role changed successfully.")
    return redirect("Ahome.manageusers") 