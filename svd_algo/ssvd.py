import numpy as np
import svd_algo.svd as svd


def svd_shuffle(matrix, block_size=16):
    """
    Using extended shuffling for single block here

    :param numpy.array matrix:
    :return:
    """

    M, N = matrix.shape
    X = []
    for i in range(M // block_size):
        a = i * block_size
        for j in range(N // block_size):
            b = j * block_size
            cell = matrix[a:a + block_size, b:b + block_size]

            cell = cell.reshape((1, -1))
            X.append(cell[0])
    X = np.array(X)
    return X


def svd_unshuffle(X, old_size, block_size=16):
    """
    Unshuffling the array

    :param block_size:
    :param numpy.ndarray X:
    :return:
    """
    m, n = old_size

    m = m - (m % block_size)
    n = n - (n % block_size)

    height, width = m // block_size, n // block_size

    A = [None] * height

    for i in range(len(X)):
        row = X[i].reshape((block_size, block_size))
        if (i * block_size) % n == 0:
            A[(i * block_size) // n] = row.copy()
        else:
            A[(i * block_size) // n] = np.hstack([A[(i * block_size) // n], row])

    res = A[0]
    for i in range(1, len(A)):
        res = np.vstack([res, A[i]])

    return res


if __name__ == "__main__":
    import numpy as np
    from PIL import Image

    img = Image.open('../test_image.jpg')

    imggray = img.convert('LA')
    imgmat = np.array(list(imggray.getdata(band=0)), float)
    imgmat.shape = (imggray.size[1], imggray.size[0])
    imgmat = np.array(imgmat, dtype=float)

    matrix = np.array([[3, 2, 0, -1, 3], [8, 21, 2, 3, 7], [-1, 1, 2, 0, 2], [7, 0, 9, 21, 3]], dtype='float64')

    # U, sigma, V = ssvd.preprocess_ssvd(np.array(imgmat, dtype='float64'), block_size=8)
    #
    # X = svd_shuffle(matrix, block_size=2)
    # print(X)
    #
    # u, s, v = svd.svd(X)
    #
    # X = u.dot(s).dot(v.T)
    # A = svd_unshuffle(X, matrix.shape, block_size=2)
