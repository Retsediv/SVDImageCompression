from random import normalvariate
from numpy.linalg import norm

import numpy as np
from math import sqrt


def svd_shuffle(matrix):
    """
    Using extended shuffling here

    :param numpy.array matrix:
    :return:
    """

    # Old implementation...
    # X = np.zeros((1, n * m))
    #
    # for i in range(m):
    #     for j in range(n):
    #         X[np.math.floor(i / n) * n + np.math.floor(j / n)][(i % n) * n + (j % n)] = matrix[i][j]

    m, n = matrix.shape
    X = np.reshape(matrix, (1, m * n))
    return X


def process_svd(matrix, block_size=16):
    """
    Divide on blocks, shuffle, use svd and then shuffle back

    :param matrix numpy.array
    :return: U, S, V
    """

    m, n = matrix.shape
    X = []

    # divide on blocks
    for i in range(0, m, block_size):
        row = []

        for j in range(0, n, block_size):
            m_limit = i + block_size
            n_limit = j + block_size
            if m_limit > m:
                break
                m_limit = m
            if n_limit > n:
                break
                n_limit = n

            block = matrix[i:m_limit, j:n_limit]
            shuffled_block = svd_shuffle(block)

            for value in shuffled_block[0]:
                row.append(value)

            # print()

        # print("row: ", row)
        X.append(row)

    print("X: ", X)
    # print(svd(np.array(X)))


if __name__ == "__main__":
    matrix = np.array([[3, 2, 0, -1], [8, 2, 3, 7], [1, 2, 0, -2], [7, 0, -21, 3]], dtype='float64')
    process_svd(matrix, 2)
