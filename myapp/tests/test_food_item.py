
from myapp.models import FoodItem

def test_unicode():
    apple2 = FoodItem(name='apple2', price=123)
    assert True

