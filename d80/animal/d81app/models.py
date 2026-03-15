from dataclasses import dataclass
from typing import List
from typing import List, Optional


@dataclass
class AuditData:
    """
    Base class simulating audit fields in Django models.
    """
    created_at: str
    updated_at: str
    created_by: str

    def __init__(self, created_by, created_at, updated_at):
        self.created_by = created_by
        self.created_at = created_at
        self.updated_at = updated_at


class CatalogProduct(AuditData):
    """
    Product model that inherits from AuditData.
    - Auto-increment id
    - Stored in-memory (Product.objects)
    """
    _next_id: int = 1
    objects: List["Product"] = []

    # def __init__(self, name: str, price: float, created_by: str,
    # created_at: str | None = None, updated_at: str | None = None):
    def __init__(self, name: str, price: float, created_by: str,
                 created_at: Optional[str] = None, updated_at: Optional[str] = None):
        # TODO: Assign id, call parent __init__, set fields, append to objects
        super(CatalogProduct, self).__init__(created_by, created_at, updated_at)
        self.id = CatalogProduct._next_id
        CatalogProduct._next_id = CatalogProduct._next_id + 1
        self.name = name
        self.price = price
        CatalogProduct.objects.append(self)

    @classmethod
    def get_all(cls) -> List[str]:
        """
        TODO: Return all products in the format:
        "ID: <id>, Name: <name>, Price: <price>, Created By: <created_by>"
        """
        # return [str(product) for product in cls.objects]
        return cls.objects

    @classmethod
    def reset_store(cls) -> None:
        """
        TODO: Reset objects list and id counter (useful for tests).
        """
        cls._next_id = 1
        cls.objects = []

    def __str__(self) -> str:
        """
        TODO: Return string representation of product
        "ID: <id>, Name: <name>, Price: <price>, Created By: <created_by>"
        """
        return "ID: {}, Name: {}, Price: {}, Created By: {}".format(self.id, self.name, self.price, self.created_by)
