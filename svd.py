from random import normalvariate
from numpy.linalg import norm

import numpy as np
from math import sqrt


def matrix_multiply(A, B):
    return [[sum(a * b for a, b in zip(B_row, A_col)) for A_col in zip(*A)] for B_row in B]


def get_identity(size):
    return [[0 if _ != i else 1 for _ in range(size)] for i in range(size)]


def get_martix_size(matrix):
    try:
        m = len(matrix[0])
    except IndexError:
        m = 0

    n = len(matrix)
    return m, n


def get_transpose(matrix):
    return list(zip(*matrix))


def randomUnitVector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    norm = sqrt(sum(x * x for x in unnormalized))
    return [x / norm for x in unnormalized]


def svd_1d(A, epsilon=1e-10):
    n, m = A.shape
    x = randomUnitVector(m)
    lastV = None
    currentV = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        lastV = currentV
        currentV = np.dot(B, lastV)
        currentV = currentV / norm(currentV)

        if abs(np.dot(currentV, lastV)) > 1 - epsilon:
            print("converged in {} iterations!".format(iterations))
            return currentV


def svd(A, k=None, epsilon=1e-10):
    n, m = A.shape
    svdSoFar = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrixFor1D = A.copy()

        for singularValue, u, v in svdSoFar[:i]:
            matrixFor1D -= singularValue * np.outer(u, v)

        v = svd_1d(matrixFor1D, epsilon=epsilon)  # next singular vector
        u_unnormalized = np.dot(A, v)
        sigma = norm(u_unnormalized)  # next singular value
        u = u_unnormalized / sigma

        svdSoFar.append((sigma, u, v))

    singularValues, us, vs = [np.array(x) for x in zip(*svdSoFar)]
    return singularValues, us.T, vs


if __name__ == "__main__":
    matrix = np.array([[3, 2], [2, 3], [2, -2]], dtype='float64')
    print(svd(matrix))
