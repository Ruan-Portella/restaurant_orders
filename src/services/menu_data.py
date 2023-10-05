import csv
from models.dish import Dish
from models.ingredient import Ingredient


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.data = []
        self.read_csv(source_path)
        self.create_dish()

    def read_csv(self, source_path: str):
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            header, *data = reader

        self.data = data

    def create_dish(self):
        dishCreated = {}
        for recipe in self.data:

            if recipe[0] in dishCreated:
                dish = dishCreated[recipe[0]]
                dish.add_ingredient_dependency(Ingredient(recipe[2]),
                                               int(recipe[3]))
            else:
                dish = Dish(recipe[0], float(recipe[1]))
                dishCreated[recipe[0]] = dish
                self.dishes.add(dish)
                dish.add_ingredient_dependency(Ingredient(recipe[2]),
                                               int(recipe[3]))
        return self.dishes
