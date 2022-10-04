from django.db import models
from user.models import NewUser


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
        default=0, unique=True)
    school_email = models.EmailField(max_length=200)
    created_by = models.ForeignKey(NewUser,
                                   on_delete=models.CASCADE,
                                   related_name='school_admin')
    last_updated = models.DateTimeField(auto_now=True)

    def __int__(self):
        return self.pupil_id
