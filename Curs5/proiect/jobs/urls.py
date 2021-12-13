from django.urls import path
from jobs import views

app_name = 'jobs'

urlpatterns = [
    #path('', views.CreateJobView.as_view(), name='adaugare'),
    path('create/',views.CreateJobView.as_view(), name='adaugare'),
    path('update/<int:pk>', views.UpdateJobView.as_view(), name='modificare'),
    path('list/', views.ListJobView.as_view(), name='listare'),
    path('delete/<int:pk>/', views.delete_job, name='remove'),
]