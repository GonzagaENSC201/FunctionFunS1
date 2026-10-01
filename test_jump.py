import numpy as np
from jump import calculate_jump_distance, calculate_horizontal_speed

def test_calculate_jump_distance():
    # assert order is actual vs expected
    assert np.isclose(calculate_jump_distance(6.0, 0.8), 4.8) # shopping cart test case
    assert calculate_jump_distance(15.5, 1.4) == 21.7 # dirt bike test case
