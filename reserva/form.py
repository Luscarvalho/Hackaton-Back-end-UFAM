from django import forms

from .models import Reserva


class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaModelForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        widgets = {
            'dt_inicial': DateInput(),
            'dt_final': DateInput(),
        }
