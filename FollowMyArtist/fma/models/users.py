# '''
# Created on Mar 8, 2016
# 
# @author: TBENER
# '''
# 
# from django.db import models
# from fma.models.artists import Artist
# 
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )
# from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
# from django.core.mail import send_mail
# 
# class MyUserManager(BaseUserManager):
#     def create_user(self, email, password=None):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')
# 
#         user = self.model(
#             email=self.normalize_email(email),
#         )
# 
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
# 
#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(email,
#             password=password
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user
# 
# class FmaUser(AbstractBaseUser):
#     first_name = models.CharField(_('first name'), max_length=30, blank=True)
#     last_name = models.CharField(_('last name'), max_length=30, blank=True)
#     email = models.EmailField(_('email address'), max_length=254, blank=False, unique=True, db_index=True)  
#     is_active = models.BooleanField(_('active'), default=True,
#         help_text=_('Designates whether this user should be treated as '
#                     'active. Unselect this instead of deleting accounts.'))
#     is_admin = models.BooleanField(default=False)
#     date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
#     gender_choices = (
#         ('M', 'Male'),
#         ('F', 'Female'),
#         )
#     gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
#     date_of_birth = models.DateField(null=True, blank=True)
#     city = models.CharField(max_length=50, blank=True)
#     phone_number = models.CharField(max_length=15, blank=True)
#     description = models.TextField(blank=True)
#     
#     artists     = models.ManyToManyField(Artist)
# 
#     objects = MyUserManager()
# 
#     USERNAME_FIELD = 'email'
# 
#     class Meta:
#         verbose_name = _('user')
#         verbose_name_plural = _('users')
# 
#     def get_full_name(self):
#         full_name = '%s %s' % (self.first_name, self.last_name)
#         return full_name.strip()
# 
#     def get_short_name(self):
#         return self.first_name
# 
#     def email_user(self, subject, message, from_email=None):
#         """
#         Sends an email to this User.
#         """
#         send_mail(subject, message, from_email, [self.email])
# 
#     def __unicode__(self):
#         return self.first_name + ' ' + self.last_name
# 
#     def has_perm(self, perm, obj=None):
#         return True
# 
#     def has_module_perms(self, app_label):
#         return True
# 
#     @property
#     def is_staff(self):
#         return self.is_admin