import numpy as np
from math import sqrt
import math


def compute_sigma(evalues, m, n):
    sigma = np.zeros((m, n))

    for i in range(m):
        try:
            sigma[i, i] = evalues[i]**0.5
        except IndexError as e:
            continue

    return sigma


def compute_V(evalues, evectors):
    evectors = evectors.T

    evalues, evectors = zip(*sorted(zip(evalues, evectors), reverse=True))
    evectors = np.array(evectors)

    V = evectors.T

    return V


def compute_U(matrix, S, V, n):
    UT = np.zeros((len(S), len(matrix)))

    n, m = S.shape

    for i in range(min(n, m)):
        d = np.dot((1 / S[i, i]), matrix)
        UT[i] = np.dot(d, V[i])

    U = UT.T

    return U


def svd(matrix):
    n, m = matrix.shape

    # Compute eigenvalues of A * A(T)
    AAT = matrix.dot(matrix.T)
    eigenvalues = np.linalg.eigvals(AAT)

    # Compute eigenvectors of A(T) * A
    ATA = matrix.T.dot(matrix)
    values, eigenvectors = np.linalg.eig(ATA)

    # Compute Sigma(S) -> middle diagonal matrix
    S = compute_sigma(eigenvalues, n, m)

    # Compute V -> right orthogonal matrix
    V = compute_V(values, eigenvectors)
    V = V.T

    # Compute U -> left orthogonal matrix
    U = compute_U(matrix, S, V, n)

    return U, S, V.T


if __name__ == "__main__":
    # matrix = np.array([
    #     [3.0, 2.0`, 8.0, 2.0, 0.0, -1.0, 3.0, 7.0],
    #     [1, 2, 3, 4, 5, 6, 7, 8],
    #     [8, ],
    #     [1.0, 2.0, 7.0, 0.0, 0.0, -2.0, -21.0, 3.0]
    # ])
    matrix = np.array([
        [5, 53,],
        [-1, 7],
        [1, 2],
    ])

    u, s, v = svd(matrix)
    # print(u)
    # print(s)
    # print(v)

    print(u.dot(s).dot(v.T))
