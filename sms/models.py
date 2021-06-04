from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.TextField(default='', null=True, blank=True)
    price = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True, default=0, blank=True)
    image = models.ImageField(upload_to='sms_images/', blank=False, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_quantity = models.IntegerField(blank=True, null=True)
    receive_by = models.CharField(max_length=30, null=True)
    issue_by = models.CharField(max_length=30, null=True)
    issue_quantity = models.IntegerField(default=0, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_csv = models.BooleanField(default=False)
    tags_id = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

