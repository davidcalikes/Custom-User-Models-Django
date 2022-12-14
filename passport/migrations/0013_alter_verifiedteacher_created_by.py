# Generated by Django 3.2.15 on 2022-10-07 08:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('passport', '0012_rename_teacherverify_verifiedteacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifiedteacher',
            name='created_by',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='teacher_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
