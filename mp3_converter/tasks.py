import youtube_dl
from celery import Celery
from django.core.mail import send_mail
from django.conf import settings
from django.template import loader


app = Celery('tasks', broker='redis://localhost:6379/0', backend='redis://localhost')


@app.task(bind=True)
def downloadYoutube(url, email):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{settings.MEDIA_ROOT}youtube/%(title)s-%(upload_date)s-%(id)s.%(ext)s'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        url = info['url']
        name = info['name']
        send_email.delay(url, email, name)


@app.task
def send_email(url, email, name):
    html_message = loader.render_to_string(
        '/home/nursultan/PycharmProjects/mp3_converter/music/templates/messages.html',
        {
            'url': url,
            'name': name,
        }
    )
    send_mail(
        'Спасибо',
        ['receiver@gmail.com'],
        fail_silently=True,
        html_message=html_message
    )
