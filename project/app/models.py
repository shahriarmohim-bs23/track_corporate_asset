from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Device(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('Phone', 'Phone'),
        ('Tablet', 'Tablet'),
        ('Laptop', 'Laptop'),
        ('Other', 'Other'),
    ]
    model = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100)
    device_type = models.CharField(max_length=10, choices=DEVICE_TYPE_CHOICES)
    purchase_date = models.DateField()
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.model

class DeviceLog(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_date = models.DateTimeField(auto_now_add=True)
    check_in_date = models.DateTimeField(null=True, blank=True)
    check_out_condition = models.CharField(max_length=100, null=True, blank=True)
    check_in_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.device.model} - {self.employee.user.username}'



