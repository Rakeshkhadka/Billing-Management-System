from faker import Faker

import random 
from .models import *
fake = Faker()


for _ in range(10):
    client_data = {
        'name': fake.name(),
        'email': fake.email(),
        'organization_size' : fake.random_element(ORGANIZATION_SIZE_CHOICES)[0],
        'expiry_date': fake.date(),
        'country': fake.country(),
        'status' : fake.random_element(STATUS_CHOICES)[0]
    }
    domain = client_data['name'].split(' ')[0] + 'realhrsoft.com.np'
    Client.objects.create(domain = domain, **client_data)
    SubscriptionPlan.objects.c



# number_of_users
# modules  CHOICE = MODULE_CHOICE
# price

