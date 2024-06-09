from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User
from django.core.mail import send_mail
@receiver(post_save, sender=User)
def Welcome(sender,instance,created,**kwargs):
    if created:
        send_mail(
            'Welcome',
            f'Welcome {instance.username}',
            'lewiskinyuanjue.ke@gmail.com',
            [instance.email],
            fail_silently=True,
        )
        