import pytest
import random

from libia.algorithm.kmean_clusturing import get_distance, get_closest_centroid, labelling, get_edges


@pytest.fixture()
def data() -> list[tuple[float, float]]:
    return [
        (1, 1),
        (0, 3),
        (4, 0),
        (3, 4)
    ]

@pytest.fixture()
def centroids() -> list[tuple[float, float]]:
    return [
        (2, 2),
        (3, 3),
    ]

def test_get_edges(data):
    assert get_edges(data) == (0, 4, 0, 3)

def test_get_closest_centroid(data, centroids):
    labels = [0, 0, 0, 1]
    for elem, label in zip(data, labels):
        assert get_closest_centroid(elem, centroids) == label

def test_labelling(data, centroids):
    labels = [0, 0, 0, 1]
    assert labelling(data, centroids) == labels
