# Create your views here.
# CreateView -> clasa pt adaugat date in formular
# UpdateView -> clasa pt modificat date in formular
# DeleteView -> clasa pt sters date din formular
# IndexView -> clasa pt informat cu privire la formular
# ListView -> clasa pt informatii de tip lista din db
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, ListView
from aplicatie1.models import Location
from django.contrib.auth.decorators import login_required
from aplicatie1.forms import LocationForm

class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    #fields = '__all__'
    #fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'aplicatie1/location_form.html'

    def get_success_url(self):
        return reverse('aplicatie1:listare')

    def get_form_kwargs(self):
        data = super(CreateLocationView, self).get_form_kwargs()
        data.update({'pk': None})
        return data


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    # fields = '__all__'
    #fields = ['city', 'country']
    form_class = LocationForm
    template_name = 'aplicatie1/location_form.html'

    def get_forms_kwargs(self):
        data = super(UpdateLocationView, self).get_form_kwargs()
        data.update({'pk': self.kwargs['pk']})
        return data

    def get_success_url(self):
        return reverse('aplicatie1:listare')


class ListLocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'aplicatie1/location_index.html'

    def get_queryset(self):
        return Location.objects.filter(active=1)

@login_required
def delete_location(request, pk):
    if request.user.is_authenticated:
        Location.objects.filter(id=pk).update(active=0)
    return redirect('aplicatie1:listare')
