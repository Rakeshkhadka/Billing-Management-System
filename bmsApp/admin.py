from django.contrib import admin

# Register your models here.
from .models import Client, Metrics, Subscription, SubscriptionPlan
Model_Name = [Client, Metrics, Subscription, SubscriptionPlan]
admin.site.register(Model_Name)