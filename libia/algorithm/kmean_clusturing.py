import math
import random

def get_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    x_diff = x1 - x2
    y_diff = y1 - y2
    return math.sqrt(x_diff * x_diff + y_diff * y_diff)

def get_closest_centroid(elem: tuple[float, float], centroids:list[tuple[float, float]]) -> int:
    diff = (get_distance(elem[0], elem[1], centroids[0][0], centroids[0][1]), 0)
    for i, centroid in enumerate(centroids[1:]):
        diff_candidate = get_distance(elem[0], elem[1], centroid[0], centroid[1])
        if diff_candidate < diff[0]:
            diff = (diff_candidate, i + 1)
    return diff[1]

def labelling(elems: list[tuple[float, float]], centroids:list[tuple[float, float]]) -> list[int]:
    labels = []
    for elem in elems:
        labels.append(get_closest_centroid(elem, centroids))
    return labels

def get_edges(elems: list[tuple[float, float]]) -> tuple[float, float, float, float]:
    min_x, min_y, max_x, max_y = elems[0] + elems[0]
    for elem in elems[1:]:
        min_x, min_y = [min(min_x, elem[0]), min(min_y, elem[1])]
        max_x, max_y = [max(max_x, elem[0]), max(max_y, elem[1])]
    return min_x, max_x, min_y, max_y

def init_centroids(elems: list[tuple[float, float]], n: int) -> list[tuple[float, float]]:
    centroids = []
    min_y, max_x, min_x, max_y = get_edges(elems)
    for i in range(n):
        centroids.append((random.uniform(min_x, max_x), random.uniform(min_y, max_y)))
    return centroids



def twod_kmean(n_cluster: int, data: list[list[float]], max_gen: int) -> list[float]:
    """
    K-means clustering
    :param n_cluster:
    :param data:
    :param max_gen:
    :return:
    set centroids positions bitween max D1 and max D2
    for each gen:
        label each elem in the data set to the closest centroid
        get mean dist of elem of cluster 
        recalculate centroids positions between by mean position of clustered elements coord

    """
    labeled = []


    return labeled