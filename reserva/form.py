from django import forms




class DateInput(forms.DateInput):
    input_type = 'date'

class ReservaModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = '__all__'
        widgets = {
            'my_date': DateInput(),
        }
