from django.db import models
import string
import random

def id_generator(size=10, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Machine(models.Model):
    machine_ID = models.BigAutoField( primary_key=True)
    machine_registration_no = models.CharField(max_length=255, unique=True)
    machine_name = models.CharField(max_length=255, )
    machine_current_temperature = models.CharField(max_length=255)
    
    def __str__(self):
        return self.machine_name