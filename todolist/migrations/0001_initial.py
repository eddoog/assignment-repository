# Generated by Django 4.1 on 2022-09-25 10:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import todolist.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=todolist.models.get_default_my_date)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_finished', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
