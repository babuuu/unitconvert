import pytest

from unitconvert import temperature

def test_temperature():
    # some known results
    # distance between two same points should be zero
    assert temperature.fahrenheit_to_celsius(50) == 10
    assert temperature.celsius_to_fahrenheit(10) == 50
    
    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        temperature.fahrenheit_to_celsius(1, 2)
    with pytest.raises(TypeError):
        temperature.celsius_to_fahrenheit(1, 2)       