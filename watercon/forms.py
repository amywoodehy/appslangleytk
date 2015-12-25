from django.forms import forms


class InputCSVForm(forms.Form):
    name = forms.TextInput()
    csv_file = forms.FileField(required=True)

