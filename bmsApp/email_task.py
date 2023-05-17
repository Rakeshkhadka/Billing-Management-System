from django.conf import settings
from django.core.mail import send_mail

from django.db.models import Q
from datetime import date, timedelta

from .models import *

def send_expiry_mail():
    clients = Client.objects.filter(
                    Q(expiry_date__lte = date.today()+timedelta(5))
                    &
                    Q(expiry_date__gte=date.today())
                )
    subject = "Your hms is expiring soon"
    from_email = settings.EMAIL_HOST_USER
    for client in clients:

        message = f"""Dear {client.name},

I hope this email finds you well. I am writing to bring your attention to the upcoming expiry of your HRMS (Human Resource Management System) subscription with our company. It is important to ensure continuous access and functionality of your HRMS, and therefore, we kindly request your attention to this matter.

As per our records, the HRMS subscription for your organization is scheduled to expire on {client.expiry_date}. Without renewal or extension, access to the HRMS will be restricted, and you may experience interruptions in essential HR functions, such as employee data management, attendance tracking, payroll processing, and other crucial HR processes.

To avoid any disruption to your HR operations and to maintain seamless management of your workforce, we highly recommend taking prompt action to renew or extend your HRMS subscription. Our team is available to assist you throughout the process and provide any necessary guidance or information you may require.

Please reach out to our dedicated HRMS support team at 9841234567 to discuss the renewal process, pricing, and any specific requirements your organization may have. They will be delighted to assist you in choosing the most suitable package and addressing any queries you may have.

We value your partnership and are committed to providing you with reliable and efficient HR solutions. Ensuring the uninterrupted operation of your HRMS is essential for maintaining smooth HR processes within your organization.

Thank you for your attention to this matter, and we look forward to continuing to serve you with our HRMS services.

Best regards,
HRMS
Kathmandu, Nepal"""
        
        receipient_list = [client.email]
        send_mail(subject, message, from_email, receipient_list)