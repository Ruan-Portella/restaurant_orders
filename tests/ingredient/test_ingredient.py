from src.models.ingredient import Ingredient  # noqa: F401, E261, E501
from src.models.ingredient import Restriction


# Req 1
def test_ingredient():
    ing_1 = Ingredient("queijo parmesão")
    ing_2 = Ingredient("massa de lasanha")
    ing_3 = Ingredient("massa de lasanha")
    assert ing_1.__hash__() != ing_2.__hash__()
    assert ing_1.__hash__() == ing_1.__hash__()
    assert ing_1.__eq__(ing_2) is False
    assert ing_2.__eq__(ing_3) is True
    assert ing_1.__repr__() == "Ingredient('queijo parmesão')"
    assert ing_1.name == "queijo parmesão"
    assert ing_2.name == "massa de lasanha"
    assert ing_1.restrictions == {Restriction.LACTOSE,
                                  Restriction.ANIMAL_DERIVED}
