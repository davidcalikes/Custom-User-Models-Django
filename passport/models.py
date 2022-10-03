from django.db import models
from user.models import NewUser
from django.core.validators import MinValueValidator, MaxValueValidator


class EnrolledPupil(models.Model):
    pupil_last_name = models.CharField(
        max_length=200, default='')
    pupil_first_name = models.CharField(
        max_length=200, default='')
    school_name = models.CharField(
        max_length=200, default='')
    teacher_name = models.CharField(
        max_length=200, default='')
    school_roll_no = models.CharField(
        max_length=200, default='')
    pupil_id = models.PositiveIntegerField(
        default=0, validators=[
            MinValueValidator(0),
            MaxValueValidator(99999999)],
        unique=True)
    slug = models.SlugField(max_length=999999, unique=True)
    school_email = models.EmailField(max_length=200)
    created_by = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='role')
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pupil_last_name
