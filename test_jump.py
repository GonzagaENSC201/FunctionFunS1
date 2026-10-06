import numpy as np
from jump import calculate_jump_distance, calculate_horizontal_speed

def test_calculate_jump_distance():
    # assert order is actual vs expected
    actual_result = calculate_jump_distance(6.0, 0.8)
    assert np.isclose(actual_result, 4.8) # shopping cart test case
    assert calculate_jump_distance(15.5, 1.4) == 21.7 # dirt bike test case

def test_calculate_horizontal_speed():
    assert np.isclose(calculate_horizontal_speed(12, 1.5), 8.0)
    assert np.isclose(calculate_horizontal_speed(20, 2), 10.0)
    assert np.isclose(calculate_horizontal_speed(0, 3), 0.0)
