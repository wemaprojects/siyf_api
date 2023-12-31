# Generated by Django 5.0 on 2023-12-10 16:33

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('ip', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='HeaderNews',
            fields=[
                ('id', models.CharField(default=core.models.gen_uuid4_hexed, max_length=1024, primary_key=True, serialize=False)),
                ('image', models.ImageField(default=core.models.gen_uuid4_hexed, upload_to='')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.CharField(default=core.models.gen_uuid4_hexed, max_length=1024, primary_key=True, serialize=False)),
                ('image', models.ImageField(default=core.models.gen_uuid4_hexed, upload_to='')),
                ('text', models.TextField()),
            ],
        ),
    ]
