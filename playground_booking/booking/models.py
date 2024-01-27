from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='custom_user_groups')
    user_permissions = models.ManyToManyField(
        Permission, related_name='custom_user_groups')
    phone_number = models.CharField(max_length=15, blank=False)
    is_creator = models.BooleanField(default=False)
    is_booker = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='images/user_images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    
    def sync_permissions(self):
        # Синхронизация групп и прав доступа
        self.user_permissions.set(Permission.objects.filter(group__in=self.groups.all()))


class Playground(models.Model):
    name = models.CharField(max_length=50, blank=False, null=True)
    admin = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, blank=False, null=True)
    phone_number = models.CharField(max_length=15, blank=False, null=True)
    price = models.FloatField(default=0, blank=False)
    width = models.IntegerField(blank=False, null=True)
    height = models.IntegerField(blank=False, null=True)
    reservation_status = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(
        upload_to='images/playground_images/', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.admin.username} - {self.id}'


class Booking(models.Model):
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_confirmed = models.BooleanField(default=False)
    admin_status = models.CharField(max_length=15, choices=(
        ('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')), default='pending')
    total_price = models.IntegerField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} - {self.playground.name} - {self.id}'
    
