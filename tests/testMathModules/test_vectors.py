import pytest
from libia.mathModules import vectors

def test_get_norm():
    v = [4, 3]
    assert vectors.get_norm(v) == 5
    assert vectors.get_norm([0, 0, 0]) == 0

def test_normalize_vector():
    v = [4, 3]
    assert vectors.normalize_vector(v) == [0.8, 0.6]
    assert vectors.normalize_vector([0, 0, 0]) == [0, 0, 0]
