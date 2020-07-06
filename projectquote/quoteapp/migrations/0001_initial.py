# Generated by Django 3.0.6 on 2020-06-29 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=40)),
                ('body', models.TextField()),
                ('context', models.CharField(blank=True, max_length=200)),
                ('source', models.CharField(blank=True, max_length=47)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
