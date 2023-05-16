from django.contrib import admin

# Register your models here.
from .models import Client, Metrics, Subscription, SubscriptionPlan, History
Model_Name = [Client, Metrics, Subscription, SubscriptionPlan, History]
admin.site.register(Model_Name)