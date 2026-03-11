# from django.db import models

# Q4. Simulate ORM `.all()` Behavior

# Create your models here.
class Animal():
    # class-level list to store all objects
    objects = []

    # constructor to create Animal objects
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        #Animal.objects.append(self)

    # create a Java equivalent static methos
    @classmethod
    def all(cls):
        """
                Return all Animal objects.
                """
        # TODO: return cls.objects
        return cls.objects

    def __str__(self):
        # TODO: return string in format "<id> - <name> - <age>"
        return "{} - {}  - {}".format(self.id, self.name, self.age)

    @classmethod
    def get_all_animals(cls):
        return cls.objects
    @classmethod
    def get_animal_by_id(cls, id):
        for animal in cls.get_all_animals():
            if animal.id == id:
                return animal



# Pre-populate with 3 objects
# TODO: Add 3 animals here to Animal.objects
Animal.objects.append(Animal(1,"Dog",5))
Animal.objects.append(Animal(2,"Cat", 3))
Animal.objects.append(Animal(3, "Rabbit", 4))
