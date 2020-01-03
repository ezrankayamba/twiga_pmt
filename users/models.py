from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from . import choices
from django.urls import reverse


class Role(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('role-list')


class RolePrivilege(models.Model):
    role = models.ForeignKey(to=Role, related_name='privileges', on_delete=models.CASCADE)
    privilege = models.CharField(max_length=40, choices=choices.PRIVILEGE_CHOICES)

    class Meta:
        unique_together = [['role', 'privilege']]


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    change_password = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)
    created_by = models.ForeignKey(to=User, related_name="created_profiles", on_delete=models.PROTECT, null=True)
    updated_by = models.ForeignKey(to=User, related_name="updated_profiles", on_delete=models.PROTECT, null=True)
    role = models.ForeignKey(to=Role, related_name='profiles', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
