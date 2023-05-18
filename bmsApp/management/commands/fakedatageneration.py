from typing import Any, Optional
from django.core.management.base import BaseCommand
from faker import Faker

from bmsApp.models import *
fake = Faker()

class Command(BaseCommand):
    help = 'create fake data for testing'
    

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        subscription_plan=SubscriptionPlan.objects.all()

        subscription_list =  []
        metrics_list = []
        for _ in range(30):
            client_data = {
                'name': fake.name(),
                'email': fake.email(),
                'organization_size' : fake.random_element(ORGANIZATION_SIZE_CHOICES)[0],
                'expiry_date': fake.date(),
                'country': fake.country(),
                'status' : fake.random_element(STATUS_CHOICES)[0]
            }
            domain = 'https://' + client_data['name'].split(' ')[0].lower() + '.realhrsoft.com.np'
            Client.objects.create(domain = domain, **client_data)

            subscription_plan_data = {
                'number_of_users' : fake.random_number(digits=3, fix_len=False),
                'modules': fake.random_element(MODULE_CHOICE)[0],
                'price': fake.random_number(digits=5, fix_len=True)
            }
            SubscriptionPlan.objects.create( **subscription_plan_data)






        for i in range(30):
            subscription_list.append(
                Subscription(
                client =  clients[i],
                status =  fake.random_element(SUBSCRIPTION_STATUS)[0],
                model =  fake.random_element(SUBSCRIPTION_MODEL)[0],
                subscription_plan = subscription_plan[i]
            ))

            metrics_list.append(
                Metrics(
                    client =  clients[i],
                    ram_usage = fake.random_int(min=1, max=8),
                    hard_disk_usage = fake.random_int(min=256, max=2048),
                    number_of_users = fake.random_number(digits=3),
                    number_of_organizations = fake.random_int(min=1, max=5),
                )
            )

        Subscription.objects.bulk_create(subscription_list, ignore_conflicts=True)
        Metrics.objects.bulk_create(metrics_list, ignore_conflicts=True)
