from .models import Blog, Car
from django_seed import Seed
from random import randint

car_names = ("Mercedes", "Toyota", "Audi", "Honda", "Nissan", )
# Initializing the seed
seeder = Seed.seeder()

seeder.add_entity(Car, 100, {
    'name': lambda x: car_names[randint(0, len(car_names) - 1)]
})



def execute():
    seeder.execute()
    print("Seeding completed")