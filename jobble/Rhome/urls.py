from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='Rhome.index'),
 path('postjobs', views.postjobs, name='Rhome.postjobs'),
 path('searchcandidates', views.searchcandidates, name='Rhome.searchcandidates'),
  path('organizeapplicants', views.organizeapplicants, name='Rhome.organizeapplicants'),
 ]