# Generated by Django 3.2.12 on 2025-01-10 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0003_photofromexternal'),
    ]

    operations = [
        migrations.CreateModel(
            name='form_submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('user_password', models.CharField(max_length=30)),
            ],
        ),
    ]
