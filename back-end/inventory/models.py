from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Item(models.Model):
    CATEGORIES = [
        ('Body', 'Body'),
        ('Hair','Hair'),
        ('Makeup','Makeup'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=6, choices=CATEGORIES)
    expiration_date = models.DateField()
    is_expired = models.BooleanField()
    finish_date = models.DateField(blank=True, null=True)
    is_finished = models.BooleanField()

    '''def finish_product(self):
        self.finish_date = timezone.now()
        self.save()

    def is_Expired(self):
        if self.expiration_date < timezone.now():
            self.is_expired = True
        else:
            self.is_expired = False
        self.save()'''






