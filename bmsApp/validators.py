import re
from django.core.exceptions import ValidationError

def validate_email(email):
    if not re.search(r'^[A-Za-z0-9_.\-]+@[A-Za-z0-9.-]+$', email):
        raise ValidationError("Invalid email format")