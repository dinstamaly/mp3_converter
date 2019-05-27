from __future__ import unicode_literals
from .forms import DownloadForm
from .models import Music
from mp3_converter.tasks import *
from django.shortcuts import render

# Create your views here.


def field(request):
    form = DownloadForm(request.POST or None)
    if form.is_valid():
        url = form.cleaned_data.get('url')
        email = form.cleaned_data.get('email')
        Music.objects.create(url=url, email=email)
        downloadYoutube.delay(url, email)
        return render(request, 'base.html', {'form': form, 'success': 'Check your email {}'.format(email)})
    else:
        form = DownloadForm()
        return render(request, 'base.html', {'form': form})



