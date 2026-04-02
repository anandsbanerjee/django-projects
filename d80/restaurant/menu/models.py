from django.core.checks import Tags
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


class Tag(models.Model):
    name = models.CharField(max_length=100)

class MenuItem(TimeStampedModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_available = models.BooleanField(default=True)

    """
        This is 1-TO-MANY Cardinality. For one Category, there could be many MenuItems
        Thus following line creates a category object so Menutem.category refers to the 
        category model info for that MenuItem.
        
        related_name = 'items' enables reverse FK where in category model gets a MenuItem object 
        and stored in the object name 'items' and can be accessed as Category.items
    """
    category = models.ForeignKey(Category,
                                 on_delete=models.CASCADE,
                                 related_name='items')
    """
        Commenting becase implemented a base model in core app as part of Class 7.
        file:///C:/Users/futur/OneDrive/Scaler/PYTHON/Academy-Feb26-Python-Backend-LLD-Batch/Class-07-Inheritance-IDs-Custom-Queries/index.html
    """
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    """
        ManyToMany cardinality with Tags
    """
    tags = models.ManyToManyField(
                                    Tag,
                                    related_name='menuitems',
                                    blank=True
                                  )

    def __str__(self):
        return "{} - {}".format(self.id, self.name)

