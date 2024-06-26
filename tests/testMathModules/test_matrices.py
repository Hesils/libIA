from libia.mathModules.matrices import calculate_covariance_matrix

def test_cov_matrice():
    m = [
        [1, 3, -1],
        [1, 0, -1]
    ]
    expected = [
        [8 / 3, 2/3],
        [2/3, 2/3]
    ]
    assert calculate_covariance_matrix(m) == expected