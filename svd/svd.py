import numpy as np
from math import sqrt


def compute_sigma(evalues, m, n):
    sigma = np.ndarray((m, n))

    sigma = np.zeros((m, n))
    for i in range(len(sigma)):
        sigma[i][i] = np.math.sqrt(evalues[i])

    return sigma


def compute_V(evalues, evectors):
    evectors = evectors.T

    evalues, evectors = zip(*sorted(zip(evalues, evectors), reverse=True))
    evectors = np.array(evectors)

    V = evectors.T

    return V


def compute_U(matrix, S, V, n):
    U = np.ndarray((n, n))

    for i in range(n):
        vector = matrix.dot(V[i])
        vector = (1 / S[i, i]) * vector
        U[i] = vector

    U = U.T

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
    matrix = np.array([
        [3.0, 2.0, 8.0, 2.0, 0.0, -1.0, 3.0, 7.0],
        [1.0, 2.0, 7.0, 0.0, 0.0, -2.0, -21.0, 3.0]
    ])

    u, s, v = svd(matrix)
    print(u.dot(s).dot(v.T))
