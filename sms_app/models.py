from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name


category_choices = [('Furniture', 'Furniture'), ('Sport', 'Sport'),
                    ('Accessories Auto', 'Accessories Auto'), ('Movies', 'Movies')]


class Stock(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(default='', null=True, blank=True)
    price = models.IntegerField("Unit Price",null=True, blank=True)
    category = models.CharField('Category', max_length=40, blank=True, null=True, choices=category_choices)
    quantity_before = models.IntegerField(null=True, default=0, blank=True)
    quantity = models.IntegerField(null=True, default=0, blank=False)
    quantity_calc = models.IntegerField('Total Q',null=True, default=0, blank=True)
    image = models.ImageField(upload_to='sms_images/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    quantity_required = models.IntegerField('Q Required', blank=False, null=True)
    # user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    receive_quantity = models.IntegerField('Q Received', blank=False, null=True)
    receive_by = models.CharField(max_length=30, null=True, blank=True)
    issue_by = models.CharField(max_length=30, null=True, blank=True)
    issue_quantity = models.IntegerField(default=0, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    export_to_csv = models.BooleanField(default=False)
    tags_id = models.ManyToManyField(Tag, blank=True)

# if you want to use calculated field you should remove field from form & its done

    def _get_quantity(self):
        return self.quantity
    quantity_before = property(_get_quantity)

    def _get_total_quantity(self):
        x = self.quantity + self.receive_quantity
        return x
    quantity_calc = property(_get_total_quantity)

    def _get_issue_by(self):
        return self.receive_by
    issue_by = property(_get_issue_by)

    def _get_issue_quantity(self):
        if self.quantity_required and self.receive_quantity:
            x = self.quantity_required - self.receive_quantity
            return x
    issue_quantity = property(_get_issue_quantity)

    def __str__(self):
        return self.name
