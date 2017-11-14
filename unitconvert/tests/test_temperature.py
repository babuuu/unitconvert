import pytest

from unitconvert.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius

def test_temperature():
    # some known results
    # distance between two same points should be zero
    assert fahrenheit_to_celsius(50) == 10
    assert celsius_to_fahrenheit(10) == 50
    
    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        fahrenheit_to_celsius(1, 2)
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(1, 2)       