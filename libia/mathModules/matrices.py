from statistics import mean

def add_matrix(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    matrix = []
    for va, vb in zip(a, b):
        matrix.append([vva + vvb for vva, vvb in zip(va, vb)])
    return matrix

def calculate_covariance_matrix(m: list[list[float]]) -> list[list[float]]:
    # Covariance entre deux variables: mean(ab) - (mean(a)*mean(b))
    # Pour deux vecteurs, mean(ab) = mean(sum([x for x in v]))
    # Pour deux vecteurs, mean(v) = mean(sum([v]))²
    cov_matrix = []
    means = [mean(v) for v in m]
    # Pour chaque vecteur, calculer la covariance avec chaque autre vecteur
    for v_index, v in enumerate(m):
        v_cov = []
        for w_index, w in enumerate(m):
            # Variance when v == w
            v_cov.append(mean(a * b for a, b in zip(v, w)) - means[v_index] * means[w_index])
        cov_matrix.append(v_cov)
    return cov_matrix

# GPT version
# import numpy as np
#
#
# def cov_matrice(m):
#     m = np.array(m)
#     means = np.array([mean(v) for v in m])
#
#     # Calculer la matrice des produits
#     products = np.dot(m, m.T)
#
#     # Calculer la matrice de covariance
#     cov_matrix = products / m.shape[1] - np.outer(means, means)
#
#     return cov_matrix
