# Generated by Django 3.0.6 on 2020-05-29 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drugMusicApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=100)),
                ('Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='drugMusicApp.profile')),
            ],
        ),
    ]
