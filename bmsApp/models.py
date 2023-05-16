from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
ORGANIZATION_SIZE_CHOICES = (
    ('small','Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
)

STATUS_CHOICES = (
    ('verified','Verified'),
    ('unverified', 'Unverified'),
)

SUBSCRIPTION_STATUS = (
    ('due', 'Due'),
    ('paid', 'Paid'),
)

SUBSCRIPTION_MODEL = (
    ('1 month', 'One Months'),
    ('3 months', 'Three Months'),
    ('6 months', 'Six Months'),
    ('12 months', 'Twelve Months'),
)

MODULE_CHOICE = (
    ('payroll', 'PayRoll'),
    ('leave', 'Leave'),
    ('appraisal', 'Appraisal'),
    ('attendance', 'Attendance'),
)


class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    modified_at=models.DateTimeField(auto_now=True)

    class Meta:
        abstract=True
       
       
class Client(BaseModel):
    name               = models.CharField(max_length=255)
    email              = models.EmailField()
    domain             = models.URLField()
    organization_size  = models.CharField(choices=ORGANIZATION_SIZE_CHOICES, max_length=6)
    expiry_date        = models.DateField()
    country            = models.CharField(max_length=50)
    status             = models.CharField(choices=STATUS_CHOICES, max_length=10)
    
    def __str__(self):
        return f"{self.name} | {self.email}"
    
    class Meta:
        unique_together = ['name', 'email']


class SubscriptionPlan(BaseModel):
    number_of_users = models.PositiveIntegerField()
    modules = models.CharField(choices=MODULE_CHOICE, max_length=10)
    price    = models.PositiveBigIntegerField()
    
    
class Subscription(BaseModel):
    client      = models.OneToOneField(Client,on_delete=models.CASCADE)
    status      = models.CharField(choices=SUBSCRIPTION_STATUS, max_length=10)
    model       = models.CharField(choices=SUBSCRIPTION_MODEL, max_length=10)
    subscription_plan = models.OneToOneField(SubscriptionPlan, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.client.name} | {self.client.email} |{self.status}"
 
    
class Metrics(BaseModel):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)
    ram_usage = models.FloatField(validators=[MinValueValidator(0)],max_length=200)
    hard_disk_usage = models.FloatField(validators=[MinValueValidator(0)],max_length=200)
    number_of_users = models.PositiveIntegerField()
    number_of_organizations = models.PositiveIntegerField()

    def __str__(self):
        return self.number_of_users
    


class History(BaseModel):
    remarks = models.TextField()