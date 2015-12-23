from django.forms import forms


class InputCSV(forms.Form):
    csv_file = forms.FileField()

    def is_valid(self):
        return True