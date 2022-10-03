from django.db import models
from django.contrib.auth.models import AbstractUser


TYPE_CHOICES = (
               ("pupil", "pupil"),
               ("parent", "parent"),
               ("teacher", "teacher"),
               ("school", "school"),
                    )


class NewUser(AbstractUser):
    user_type = models.CharField(choices=TYPE_CHOICES, max_length=20)
