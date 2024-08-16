from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from django.dispatch import receiver, Signal
from django.core.cache import cache
from django.core.mail import send_mail
from django.conf import settings

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user,**kwargs):
    ct = cache.get('count', 0, version = user.pk)
    newcount = ct + 1
    cache.set('count', newcount, 60*60*24, version = user.pk)
    print(user.pk)

user_registered = Signal()

@receiver(user_registered)
def send_welcome_email(sender, instance, **kwargs):
    subject = 'Welcome to Our Website'
    message = f'Hello {instance.username}, thank you for registering!'
    from_email = 'webhazards@gmail.com'
    recipient_list = [instance.email]
    
    send_mail(subject, message, from_email, recipient_list)