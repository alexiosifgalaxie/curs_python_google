from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from jobs.forms import JobForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


from jobs.models import Job
# Create your views here.

class CreateJobView(LoginRequiredMixin, CreateView):
    model = Job
    #fields='__all__'
    form_class = JobForm
    template_name = 'jobs/jobs_form.html'

    def get_form_kwargs(self):
        variable_to_send = super(CreateJobView, self).get_form_kwargs()
        variable_to_send.update({'pk': None})
        return variable_to_send

    def get_success_url(self):
        return reverse('jobs:adaugare')

class UpdateJobView(LoginRequiredMixin, UpdateView):
    model = Job
    #fields = '__all__'
    form_class = JobForm
    template_name = 'jobs/jobs_form.html'

    def get_form_kwargs(self):
        variable_to_send = super(UpdateJobView, self).get_form_kwargs()
        variable_to_send.update({'pk':self.kwargs['pk']})
        return variable_to_send

    def get_success_url(self):
        return reverse('jobs:adaugare')

class ListJobView(LoginRequiredMixin, ListView):
    model = Job
    template_name = 'jobs/jobs_index.html'

    def get_queryset(self):
        return Job.objects.filter(active=1)

@login_required
def delete_job(request, pk):
    if request.user.is_authenticated:
        Job.objects.filter(id=pk).update(active=0)
    return redirect('jobs:listare')
