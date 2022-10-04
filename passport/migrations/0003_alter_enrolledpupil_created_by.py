# Generated by Django 3.2.15 on 2022-10-02 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passport', '0002_alter_enrolledpupil_pupil_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enrolledpupil',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='role', to=settings.AUTH_USER_MODEL),
        ),
    ]