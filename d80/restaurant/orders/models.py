from datetime import timedelta

from django.db import models
from core.models import TimeStampedModel
from django.db.models import Q
from django.utils import timezone
from menu.models import MenuItem


# Create your models here.
class OrderQuerySet(models.query.QuerySet):
    def completed(self):
        return self.filter(status='Completed')

    def in_complete(self):
        return self.filter(~Q(status='completed') & ~Q(status='confirmed'))

class Order(TimeStampedModel):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20,
                              choices=STATUS_CHOICES,
                              default='pending'
                              )
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(blank=True)

    """
        Commenting becase implemented a base model in core app as part of Class 7.
        file:///C:/Users/futur/OneDrive/Scaler/PYTHON/Academy-Feb26-Python-Backend-LLD-Batch/Class-07-Inheritance-IDs-Custom-Queries/index.html
    """
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    """
        Implementing Many-To-Many cardinality with MenuItems using OrderItem model
    """
    menu_items = models.ManyToManyField(
                                        MenuItem,
                                        through= 'OrderItem',
                                        related_name='orders'
                                        )

    objects = OrderQuerySet.as_manager()

    def __str__(self):
        return "Order #{} - {}".format(self.id, self.customer_name)


# Proxy model implementation using a manager - > Use same model but with a different behaviour
class RecentOrderManager(models.Manager):
    def get_queryset(self):
        week_ago = timezone.now() - timedelta(days=7)
        return super().get_queryset().filter(created_at__gte=week_ago)

class RecentOrder(Order):
    objects = RecentOrderManager()
    class Meta:
        proxy = True
        ordering = ['-created_at']


# Custom Raw SQL Query
class OrderManager(models.Manager):
    def ranked_orders_raw(self):
        query = """
            SELECT
                id,
                customer_name,
                status,
                total_amount,
                RANK() OVER (
                    PARTITION BY status
                    ORDER BY total_amount DESC
                ) AS status_rank
            FROM orders_order
        """
        return self.raw(query)

class OrderSpl(Order):
    objects = OrderManager()
    class Meta:
        proxy = True


"""
    Testing Cardinalities - 
    file:///C:/Users/futur/OneDrive/Scaler/PYTHON/Academy-Feb26-Python-Backend-LLD-Batch/Class-08-Cardinalities-N1-Migrations/index.html
    This will do following:
        a) Create a referce of Order model in OrderInvoice and store it in 'order'
        b) as we are using related_name attribute, it DJANGO framework creates a reverse FK and creates a refernce of OrderInvoice
           in Order model and store it in the object 'invoice'
           
        invoice.order -> returns Order model's object
        order.invoice -> returns OrderInvoice model's object
"""
class OrderInvoice(TimeStampedModel):
    invoice_number = models.CharField(max_length=20, unique=True)

    # Defining cardinality using OneToOne Field
    order = models.OneToOneField(Order,
                                 on_delete=models.CASCADE,
                                 related_name='invoice'
                               )
"""
    Through model class to join MenuItems and Order model
    MenuItem 1 : n OrderItem n : 1 Order
"""

class OrderItem(TimeStampedModel):
    order = models.ForeignKey(
                                Order,
                                on_delete=models.CASCADE,
                                related_name='items'
                              )

    menu_item = models.ForeignKey(
                                    MenuItem,
                                    on_delete=models.PROTECT,
                                    related_name='items'
                                )
    # Extra fields on the relationship!
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ['order', 'menu_item']


