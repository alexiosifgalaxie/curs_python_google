from django import forms
from aplicatie1.models import Location

class LocationForm(forms.ModelForm):
        class Meta:
                model = Location
                fields = ['city', 'country']  #nu trebuie neaparat lista, merge si set

        def __init__(self, pk, *args, **kwargs):
                super(LocationForm, self).__init__(*args, **kwargs)
                self.pk = pk

        def clean(self):
                cleaned_data = self.cleaned_data
                city_value = cleaned_data.get('city')
                country_value = cleaned_data.get('country')
                if self.pk:
                        if Location.objects.filter(city__icontains=city_value, country__icontains=country_value).exclude(id=self.pk).exists():
                                self._errors['city'] = self.error_class(["Orasul si tare deja exists"])
                else:
                        if Location.objects.filter(city__icontains=city_value, country__icontains=country_value).exists():
                                self._errors['city'] = self.error_class(["Orasul si tare deja exists"])
                return cleaned_data