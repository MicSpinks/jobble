from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
    path('jobs', views.jobs, name='home.jobs'),
    path('maps', views.maps, name='home.maps'),
    path('api/map-data/', views.map_data, name='map_data'),
    path('jobs/<int:job_id>/', views.job_view, name='home.job_view'),
]