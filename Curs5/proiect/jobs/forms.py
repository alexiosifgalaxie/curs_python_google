from django import forms
from jobs.models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(JobForm, self).__init__(*args, **kwargs)
        self.aux_pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        customer_value = cleaned_data.get('customer')
        if self.aux_pk:
            if Job.objects.filter(name__icontains=name_value, customer=customer_value).exclude(id=self.aux_pk).exists():
                self._errors['name'] = self.error_class(["JObul exista deja la aceasta companie"])
        else:
            if Job.objects.filter(name__icontains=name_value, customer=customer_value).exists():
                self._errors['name'] = self.error_class(["JObul exista deja la aceasta companie"])
        return cleaned_data
