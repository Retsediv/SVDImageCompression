import numpy as np
from math import sqrt
import math


def compute_sigma(evalues, m, n):
    """
    Compute sigma(middle) matrix of SVD

    :param evalues:
    :param m:
    :param n:
    :return:
    """
    sigma = np.zeros((m, n))

    for i in range(m):
        try:
            sigma[i, i] = evalues[i] ** 0.5
        except IndexError as e:
            continue

    return sigma


def compute_V(evalues, evectors):
    """
    Compute V(right side matrix) of SVD

    :param evalues:
    :param evectors:
    :return:
    """
    evectors = evectors.T

    evalues, evectors = zip(*sorted(zip(evalues, evectors), reverse=True))
    evectors = np.array(evectors)

    V = evectors.T

    return V


def compute_U(matrix, S, V, n):
    """
    Compute U(left side matrix) of SVD

    :param matrix:
    :param S:
    :param V:
    :param n:
    :return:
    """
    UT = np.zeros((len(S), len(matrix)))

    n, m = S.shape

    for i in range(min(n, m)):
        d = np.dot((1 / S[i, i]), matrix)
        UT[i] = np.dot(d, V[i])

    U = UT.T

    return U


def svd(matrix):
    """
    SVD decomposition algorithm
    Decompose a given matrix to 3 matrices(U * sigma * V.T)
    More here:
    https://en.wikipedia.org/wiki/Singular-value_decomposition

    :param matrix: np.array
    :return: np.array, np.array, np.array
    """
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


def get_A_approximation(U, sigma, V, rank):
    """
    Return an matrix approximation of a specific rank
    based on its SVD decomposition(U, sigma, V)

    :param U:
    :param sigma:
    :param V:
    :param rank:
    :return:
    """

    a = np.matrix(U[:, :rank])
    b = sigma[:rank]
    b = b[:rank, :rank]
    c = np.matrix(V[:rank, :])

    approximation = np.matrix(a * b * c, dtype='float64')

    return approximation


if __name__ == "__main__":
    matrix = np.array([
        [5, 53, ],
        [-1, 7],
        [1, 2],
    ])

    u, s, v = svd(matrix)
    print(u)
    print(s)
    print(v)

    print(u.dot(s).dot(v.T))
