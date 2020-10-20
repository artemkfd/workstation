from django import forms
from .models import Car


class CarForm(forms.ModelForm):
    grz = forms.CharField(label="Госномер", max_length=9)

    class Meta:
        model = Car
        exclude = ["create_date", "user_id", "is_our"]


class uploadFileForm(forms.Form):
    #title = forms.CharField(label="Название файла", max_length=100)
    file = forms.FileField(label='')


class doubles(forms.Form):
    grz = forms.TextInput()

