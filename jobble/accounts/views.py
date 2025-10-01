from django.shortcuts import render
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')



def login(request):
 template_data = {}
 template_data['title'] = 'Login'
 if request.method == 'GET':
        return render(request, 'accounts/login.html',
            {'template_data': template_data})
 elif request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST['username'],
            password = request.POST['password']
        )
        if user is None:
            template_data['error'] ='The username or password is incorrect.'
            return render(request, 'accounts/login.html',
                {'template_data': template_data})
        else:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('Ahome.index')
            elif user.role == "recruiter":
                return redirect("Rhome.index") 
            else:
                return redirect("home.index")      


# Create your views here.
from .forms import CustomUserCreationForm, CustomErrorList
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


@login_required
def edit_profile(request):
    template_data = {'title': 'Edit Profile'}
    user = request.user
    if request.method == 'GET':
        form = ProfileForm(instance=user)
        # split stored links into a list for individual input boxes
        links_list = user.links.splitlines() if user.links else []
        # split education/work into lists for editable rows
        education_list = user.education.splitlines() if getattr(user, 'education', None) else []
        work_list = user.work_experience.splitlines() if getattr(user, 'work_experience', None) else []
        template_data['form'] = form
        template_data['links_list'] = links_list
        template_data['education_list'] = education_list
        template_data['work_list'] = work_list
        return render(request, 'accounts/profile_edit.html', {'template_data': template_data})
    else:
        # collect multiple inputs named 'links' and join them into the single TextField
        links_list = request.POST.getlist('links')
        education_list = request.POST.getlist('education_lines')
        work_list = request.POST.getlist('work_lines')
        post = request.POST.copy()
        # filter empty strings and join with newline so existing logic and templates continue to work
        post['links'] = '\n'.join([l.strip() for l in links_list if l and l.strip()])
        post['education'] = '\n'.join([l.strip() for l in education_list if l and l.strip()])
        post['work_experience'] = '\n'.join([l.strip() for l in work_list if l and l.strip()])

        form = ProfileForm(post, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts.profile_detail', username=user.username)
        else:
            template_data['form'] = form
            template_data['links_list'] = links_list
            template_data['education_list'] = education_list
            template_data['work_list'] = work_list
            return render(request, 'accounts/profile_edit.html', {'template_data': template_data})


def profile_detail(request, username):
    # public profile view; recruiters may view limited fields depending on privacy flags
    user = get_object_or_404(__import__('django.contrib.auth').contrib.auth.get_user_model(), username=username)
    template_data = {'profile_user': user}
    # build a links_list for the template: split stored text by lines and normalize hrefs
    links_list = []
    raw = (user.links or '').strip()
    if raw:
        for line in raw.splitlines():
            line = line.strip()
            if not line:
                continue
            href = line
            # simple email detection
            if '@' in line and not line.lower().startswith(('http://', 'https://', 'www.')):
                href = 'mailto:' + line
            elif line.startswith('www.'):
                href = 'http://' + line
            elif not line.startswith(('http://', 'https://', 'mailto:')):
                # if it's not clearly an url, prepend http:// to be safe
                href = 'http://' + line
            links_list.append({'href': href, 'text': line})
    template_data['links_list'] = links_list
    # prepare education and work lists for the template
    edu_raw = (getattr(user, 'education', '') or '').strip()
    if edu_raw:
        template_data['education_list'] = [l.strip() for l in edu_raw.splitlines() if l.strip()]
    else:
        template_data['education_list'] = []
    work_raw = (getattr(user, 'work_experience', '') or '').strip()
    if work_raw:
        template_data['work_list'] = [l.strip() for l in work_raw.splitlines() if l.strip()]
    else:
        template_data['work_list'] = []
    # explicitly choose base template for the viewer so recruiters see recruiter layout
    if request.user.is_authenticated and getattr(request.user, 'role', '').lower() == 'recruiter':
        template_data['base_template'] = 'baseR.html'
    else:
        # allow context processor to supply default for other cases
        template_data.setdefault('base_template', None)
    return render(request, 'accounts/profile_detail.html', {'template_data': template_data})
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'accounts/signup.html',{'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('accounts.login')
        else:
            template_data['form'] = form
            return render(request, 'accounts/signup.html',
                {'template_data': template_data})