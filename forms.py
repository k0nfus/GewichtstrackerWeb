from django import forms
from .models import WeightEntry

class WeightForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['weight', 'date']  # Include 'date' field in the form
        labels = {
            'weight': 'Gewicht',
            'date': 'Datum',
        }
        date = forms.DateField(
            widget=forms.DateInput(format='%d.%m.%Y', attrs={'type': 'date'}),
            input_formats=['%d.%m.%Y']
        )
