from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='Rhome.index'),
    path('postjobs', views.postjobs, name='Rhome.postjobs'),
    path('searchcandidates', views.searchcandidates, name='Rhome.searchcandidates'),
    path('organizeapplicants', views.organizeapplicants, name='Rhome.organizeapplicants'),
    path('delete_saved_search/<int:search_id>/', views.delete_saved_search, name='delete_saved_search'),
    

]