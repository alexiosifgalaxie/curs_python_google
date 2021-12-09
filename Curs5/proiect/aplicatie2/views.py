from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from aplicatie2.forms import CompaniesForm, NewAccountForm
from aplicatie2.models import Pontaj, Companies, UserExtend
import datetime


@login_required
def newPontaj(request):
    Pontaj.objects.create(user_id=request.user.id, start_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def stopTimesheet(request):
    Pontaj.objects.filter(user_id=request.user.id, end_date=None).update(end_date=datetime.datetime.now())
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class ListCompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'

class CreateCompaniesView(LoginRequiredMixin, CreateView):
        model = Companies
        #fields = '__all__'
        form_class = CompaniesForm
        template_name = 'aplicatie2/companies_form.html'

        def get_form_kwargs(self):
            variable_to_send = super(CreateCompaniesView, self).get_form_kwargs()
            variable_to_send.update({'pk': None})
            return variable_to_send

        def get_success_url(self):
            return reverse('aplicatie2:lista')


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_form_kwargs(self):
        variable_to_send = super(UpdateCompaniesView, self).get_form_kwargs()
        variable_to_send.update({'pk': self.kwargs['pk']})
        return variable_to_send

    def get_success_url(self):
        return reverse('aplicatie2:lista')

class UpdateProfile(LoginRequiredMixin, UpdateView):
        model = UserExtend
        fields = '__all__'
        template_name = 'aplicatie/companies_form.html'

        def get_queryset(self):
                return self.model.objects.all()

        def get_success_url(self):
           return reverse('aplicatie2:lista')

class NewAccountView(LoginRequiredMixin, CreateView):
    model = UserExtend
    template_name = 'aplicatie1/location_form.html'
    form_class = NewAccountForm

    def get_form_kwargs(self):
        kwargs = super(NewAccountView, self).get_form_kwargs()
        kwargs.update({'curent user': self.request.user.id})
        return kwargs

    def form_valid(self, form):
        if form.is_valid():
            form.save(commit=False)
        return(NewAccountView, self).form_valid(form)

    def get_success_url(self):
        psw = ''.join(random)
        return reverse('aplicatie2:lista')
