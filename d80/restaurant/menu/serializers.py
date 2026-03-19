from rest_framework import serializers
from .models import Category, MenuItem

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
                    "id",
                    "name",
                    "description",
                ]
        read_only_fields = ["id"]

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "description",
            "price",
            "created_at",
            "updated_at",
            "category",
        ]

class MenuItemsWithCategorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "description",
            "price",
            "created_at",
            "updated_at",
            "category",
        ]

class MenuItemsWithCategoryFlattenSerializer(serializers.ModelSerializer):
    """
        Individually get the category models' fields and store them in variables as below
        These variables will become part of seriliazer class's fields attribute
    """
    category_id = serializers.IntegerField(source='category.id', read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    category_description = serializers.CharField(source='category.description', read_only=True)

    class Meta:
        model = MenuItem
        fields = [
            "id",
            "name",
            "description",
            "price",
            "created_at",
            "updated_at",
            "category_id",
            "category_name",
            "category_description",
        ]