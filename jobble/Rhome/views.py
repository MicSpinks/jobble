from django.shortcuts import render
from django.db import models

# Create your views here.
def index(request):
 return render(request, 'Rhome/index.html')

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