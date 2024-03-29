from django.db import models
from authentication.models import User

# Create your models here.
class Expense(models.Model):
    
    CATEGORY_OPTIONS = [
        ('ONLINE_SERVICES', 'ONLINE_SERVICES'),
        ('VACATION', 'VACATION'),
        ('GROCERIES', 'GROCERIES'),
        ('RENT', 'RENT'),
        ('CAR MORGAGE', 'CAR MORGAGE'),
        ('NETFLIX', 'NETFLIX'),
        ('OTHER', 'OTHER'),
    ]
    

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=255)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, max_length=255)
    description = models.TextField(max_length=555)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering: ['-date']

    def __str__(self):
        return str(self.owner)+'s income'
    