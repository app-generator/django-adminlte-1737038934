# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Student(models.Model):

    #__Student_FIELDS__
    first_name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    other_name = models.CharField(max_length=255, null=True, blank=True)
    residential_address = models.CharField(max_length=255, null=True, blank=True)
    gender = models.BooleanField()
    phone = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateTimeField(blank=True, null=True, default=timezone.now)
    matrix_no = models.CharField(max_length=255, null=True, blank=True)
    lga = models.ForeignKey(local_Government, on_delete=models.CASCADE)
    state = models.ForeignKey(state, on_delete=models.CASCADE)
    nationality = models.ForeignKey(nationality, on_delete=models.CASCADE)

    #__Student_FIELDS__END

    class Meta:
        verbose_name        = _("Student")
        verbose_name_plural = _("Student")


class Local_Government(models.Model):

    #__Local_Government_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Local_Government_FIELDS__END

    class Meta:
        verbose_name        = _("Local_Government")
        verbose_name_plural = _("Local_Government")


class State(models.Model):

    #__State_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__State_FIELDS__END

    class Meta:
        verbose_name        = _("State")
        verbose_name_plural = _("State")


class Nationality(models.Model):

    #__Nationality_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Nationality_FIELDS__END

    class Meta:
        verbose_name        = _("Nationality")
        verbose_name_plural = _("Nationality")



#__MODELS__END
