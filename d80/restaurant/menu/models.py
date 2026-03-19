from django.db import models

from core.models import TimeStampedModel


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name

class MenuItem(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items')
    """
        Commenting becase implemented a base model in core app as part of Class 7.
        file:///C:/Users/futur/OneDrive/Scaler/PYTHON/Academy-Feb26-Python-Backend-LLD-Batch/Class-07-Inheritance-IDs-Custom-Queries/index.html
    """
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.id, self.name)
