# Generated by Django 2.2.1 on 2019-05-27 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
