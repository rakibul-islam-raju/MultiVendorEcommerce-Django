from django.db import models
from django.contrib.auth.models import User


class BaseModels(models.Model):
    """ this is a parent model for the model needs these fields """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
    

class Vendor(BaseModels):
    name = models.CharField(max_length=254)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
