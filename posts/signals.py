from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post,User
from django.core.mail import send_mail

@receiver(post_save,sender=Post)
def Notify(sender,instance,created,**kwargs):
    if created:
        send_mail(
            'NewCreated',
            f'{instance.username} created a new post',
            'lewiskinyuanjue.ke@gmail.com',
            [instance.author.email],
            fail_silently=True,
        )