import numpy as np
import svd_algo.svd as svd


def svd_shuffle(matrix, block_size=16):
    """
    Using extended shuffling for single block here

    :param numpy.array matrix:
    :return:
    """

    n, m = matrix.shape

    count_of_blocks = np.math.floor(n / block_size) * np.math.floor(m / block_size)
    X = np.zeros((count_of_blocks, block_size*block_size))

    for i in range(m):
        for j in range(n):
            try:
                X[np.math.floor(i / block_size) * block_size + np.math.floor(j / block_size)][
                    (i % block_size) * block_size + (j % block_size)] = matrix[i][j]
            except IndexError as e:
                continue

        # print(X)

    return X


def svd_unshuffle(vector, block_size=16):
    """
    Unshuffling the array

    :param block_size:
    :param numpy.array vector:
    :return:
    """

    m, = vector.shape
    X = np.zeros((block_size, block_size))

    i = 0
    for j in range(0, m, block_size):
        X[i] = vector[j:j + block_size]
        i += 1

    return X


def preprocess_ssvd(matrix, block_size=16):
    """
    Divide on blocks, shuffle, use svd and then shuffle back

    :param block_size:
    :param matrix numpy.array
    :return: U, S, V
    """

    m, n = matrix.shape
    X = []
    c = 0

    # divide on blocks
    for i in range(0, m, block_size):

        for j in range(0, n, block_size):
            row = []

            m_limit = i + block_size
            n_limit = j + block_size
            if m_limit > m or (m_limit - i < block_size):
                break
                # m_limit = m

            if n_limit > n or (n_limit - j < block_size):
                break
                # n_limit = n

            block = matrix[i:m_limit, j:n_limit]
            # print(block)

            shuffled_block = svd_shuffle(block)
            # print(shuffled_block)
            # print()

            for value in shuffled_block[0]:
                row.append(value)

            if (len(row)) == 0:
                continue

            X.append(row)

    X = np.array(X)

    return X


def A_approximation(X, block_size=16):
    m, n = X.shape
    A = X.copy()

    for i in range(0, m):

        for j in range(0, n, block_size ** 2):
            row = X[i, j:(j + block_size ** 2)]
            print(row)

            print(svd_unshuffle(row, block_size))


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

    X = svd_shuffle(imgmat, 16)

    u, s, v = svd.svd(X)
    #
    # print(X.shape)
    # svd.svd(X)
    # print("Done")
    # X = u.dot(s).dot(v.T)

    # A_approximation(X, 2)
