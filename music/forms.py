from django import forms
from .models import Music


class DownloadForm(forms.Form):
    url = forms.CharField(max_length=250)

    class Meta:
        model = Music
        field = ('url', 'email')
