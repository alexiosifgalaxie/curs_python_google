from django import forms

from aplicatie2.models import Companies, UserExtend

class CompaniesForm(forms.ModelForm):
    class Meta:
        model = Companies
        fields= '__all__'

    def __init__(self, pk, *args, **kwargs):
        super(CompaniesForm, self).__init__(*args, **kwargs)
        self.company_pk = pk

    def clean(self):
        cleaned_data = self.cleaned_data
        name_value = cleaned_data.get('name')
        if self.company_pk:
            if Companies.objects.filter(name = name_value).exclude(id=self.company_pk).exists():
                self._errors['name'] = self.error_class(["Numele deja exists"])
        else:
            if Companies.objects.filter(name = name_value).exists():
                self._errors['name'] = self.error_class(["Numele deja exists"])
        return cleaned_data


class NewAccountForm(forms.ModelForm):
    class Meta:
        model = UserExtend
        fields = ['first_name', 'last_name', 'email', 'customer']

    def __init__(self):
        super(NewAccountForm, self).__init__()
        user_instance = UserExtend.objects.get(id=current_user)
        if user_instance.is_superuser is False:
            self.fields['customer'] = ModelChoiceField(queryset=Companies.objects.get)

    def clean(self):
        cleaned_data = self.cleaned_data
        email_value = cleaned_data.get('email')
        if UserExtend.objects.filter(email=email_value).exists():
            self._errors['email'] = self.error_class(["Emaiul deja exista, te rugam sa alegi altul"])
        return cleaned_data