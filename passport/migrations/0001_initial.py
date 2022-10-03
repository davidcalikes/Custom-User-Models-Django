# Generated by Django 3.2.15 on 2022-10-02 12:27

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EnrolledPupil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pupil_last_name', models.CharField(default='', max_length=200)),
                ('pupil_first_name', models.CharField(default='', max_length=200)),
                ('school_name', models.CharField(default='', max_length=200)),
                ('teacher_name', models.CharField(default='', max_length=200)),
                ('school_roll_no', models.CharField(default='', max_length=200)),
                ('pupil_id', models.PositiveIntegerField(default=0, unique=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999999)])),
                ('slug', models.SlugField(max_length=999999, unique=True)),
                ('school_email', models.EmailField(max_length=200, unique=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
