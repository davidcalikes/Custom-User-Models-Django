# Generated by Django 3.2.15 on 2022-10-04 11:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passport', '0004_alter_enrolledpupil_school_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrolledpupil',
            name='slug',
        ),
        migrations.AlterField(
            model_name='enrolledpupil',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_admin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='enrolledpupil',
            name='pupil_id',
            field=models.PositiveIntegerField(default=0, unique=True),
        ),
    ]
