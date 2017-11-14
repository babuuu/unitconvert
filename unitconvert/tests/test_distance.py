import pytest

from unitconvert.distance import miles_to_kilometers, kilometers_to_miles

def test_temperature():
    # some known results
    # distance between two same points should be zero
    assert round(miles_to_kilometers(1),3) == 1.609
    assert round(kilometers_to_miles(1),3) == 0.621

    # now check that we can't pass the wrong number of arguments
    with pytest.raises(TypeError):
        miles_to_kilometers(1, 2)
    with pytest.raises(TypeError):
        kilometers_to_miles(1, 2)  