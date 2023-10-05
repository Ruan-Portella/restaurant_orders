from src.models.dish import Dish
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Comida", 10.0)
    assert dish.__repr__() == "Dish('Comida', R$10.00)"

    ingredient = Ingredient("ovo")
    dish.add_ingredient_dependency(ingredient, 2)
    assert dish.name == "Comida"

    dish_2 = Dish("Comida2", 10.0)

    assert dish.__hash__() != dish_2.__hash__()
    assert dish.__hash__() == dish.__hash__()

    assert dish.__eq__(dish_2) is False
    assert dish.__eq__(dish) is True

    with pytest.raises(TypeError):
        Dish("Comida", "10.0")

    with pytest.raises(ValueError):
        Dish("Comida", -10.0)

    assert dish.get_restrictions() == ingredient.restrictions

    assert dish.get_ingredients() == {ingredient}
