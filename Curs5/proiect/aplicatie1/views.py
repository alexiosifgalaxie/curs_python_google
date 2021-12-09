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

class CreateLocationView(LoginRequiredMixin, CreateView):
        model = Location
        # fields = '__all__'
        fields = ['city', 'country']
        template_name = 'aplicatie1/location_form.html'

        def get_success_url(self):
                return reverse('aplicatie1:listare')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
        model = Location
        # fields = '__all__'
        fields = ['city', 'country']
        template_name = 'aplicatie1/location_form.html'

        def get_success_url(self):
                return reverse('aplicatie1:listare')

class ListLocationView(LoginRequiredMixin, ListView):
        model = Location
        template_name = 'aplicatie1/location_index.html'