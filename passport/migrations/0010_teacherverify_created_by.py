# Generated by Django 3.2.15 on 2022-10-06 21:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passport', '0009_auto_20221006_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherverify',
            name='created_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='teacher_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]