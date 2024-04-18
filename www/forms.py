from django import forms

from .models import Wydzial, Kierunek, Student

class WydzialForm(forms.ModelForm):
    class Meta:
        model = Wydzial
        fields = '__all__'

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control'}),
            'logo': forms.FileInput(attrs={'class':'form-control'})
        }

class KierunekForm(forms.ModelForm):
    class Meta:
        model = Kierunek
        fields = '__all__'

        widgets = {
            'nazwa': forms.TextInput(attrs={'class':'form-control'}),
            'wydzialy': forms.SelectMultiple(attrs={'class':'form-control'})
        }

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'imie': forms.TextInput(attrs={'class':'form-control'}),
            'nazwisko': forms.TextInput(attrs={'class':'form-control'}),
            'nr_albumu': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'kierunki': forms.SelectMultiple(attrs={'class':'form-control'}),
            'zdjecie': forms.FileInput(attrs={'class':'form-control'})
        }