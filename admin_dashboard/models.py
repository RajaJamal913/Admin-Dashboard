# admin_dashboard/models.py
from django.db import models
from django.conf import settings

class User(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    spent_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=20, choices=[('active', 'Active'), ('suspended', 'Suspended')])
    created_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    rates = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
# admin_dashboard/models.py
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    domain = models.CharField(max_length=255)
    expiry_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    plan = models.CharField(max_length=50)
    orders_per_month = models.IntegerField()
    user_history = models.TextField(blank=True)

    def __str__(self):
        return f"Order {self.id} for {self.user.username}"
# admin_dashboard/models.py
class BannedIP(models.Model):
    ip_address = models.GenericIPAddressField()
    domain = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=[('banned', 'Banned'), ('unbanned', 'Unbanned')])

    def __str__(self):
        return self.ip_address
# admin_dashboard/models.py
class ActivityLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    activity = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Activity by {self.user.username} on {self.timestamp}"
    
    # admin_dashboard/models.py
class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
    permissions = models.TextField()

    def __str__(self):
        return self.user.username

class API(models.Model):
    domain = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.domain

class PanelRate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.username} - {self.rate}"


class OrderPanelConfig(models.Model):
    default_features = models.BooleanField(default=False)
    maintenance_mode = models.BooleanField(default=False)
    custom_message = models.TextField(default='')
