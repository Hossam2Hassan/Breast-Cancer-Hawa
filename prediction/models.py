from django.db import models
from authentication.models import User
# Create your models here.

class prediction(models.Model):
    user=models.ForeignKey(User, verbose_name=("user"), on_delete=models.CASCADE,null=True)
    perimeter_mean=models.DecimalField(max_digits=10, decimal_places=5)
    area_mean=models.DecimalField(max_digits=10, decimal_places=5)
    area_se=models.DecimalField(max_digits=10, decimal_places=5)
    perimeter_worst=models.DecimalField(max_digits=10, decimal_places=5)
    area_worst=models.DecimalField(max_digits=10, decimal_places=5)
    result=models.CharField(max_length=20,null=True)
    