import numpy as np

from svd_algo import ssvd, svd


def compress_image(image, mode="grayscale", block_size=16, rank=20):
    """
    The main function to make a compression of the image

    :param image: np.array as a representation of image
    :param mode: 'grayscale' or 'rgb'
    :param block_size:
    :param rank: rank of approximation(the bigger rank -> better quality -> bigger size)
    :return: np.array as a representation of compressed image
    """

    possible_mode = ["grayscale", "rgb"]
    if mode not in possible_mode:
        raise ValueError(format("mode argument should be one of the: {}".format(", ".join(possible_mode))))

    if mode == "grayscale":
        X = ssvd.svd_shuffle(np.array(image, dtype='float64'), block_size)
        U, sigma, V = svd.svd(X)
        V = V.T

        reconstimg = svd.get_A_approximation(U, sigma, V, rank)

        img = ssvd.svd_unshuffle(reconstimg, image.shape, block_size)

        return img

    elif mode == "rgb":
        if len(image.shape) < 3 or image.shape[2] != 3:
            raise ValueError(
                "Image matrix should be of the size (n, m, 3) Where n, m - size of the image and 3 means three dimensions (RGB)")

        # Split into 3 layers
        layers = []
        for i in range(3):
            layers.append(image[:, :, i].copy())

        # Decompose each layer
        decomposed_layers = []

        for layer in layers:
            layer_X = ssvd.svd_shuffle(np.array(layer, dtype='float64'), block_size=16)
            U, sigma, V = svd.svd(layer_X)
            V = V.T

            decomposed_layers.append([U, sigma, V])

        # Apply approximation for each compressed_layer

        compressed_layers = []
        for dcl in decomposed_layers:
            U, sigma, V = dcl

            sl = svd.get_A_approximation(U, sigma, V, rank)
            l = ssvd.svd_unshuffle(sl, layers[0].shape, 16)

            compressed_layers.append(l)

        # Combine all 3 layers into 1 matrix and return the compressed image
        n, m = compressed_layers[0].shape
        compressedImage = np.zeros((n, m, 3), 'uint8')

        compressedImage[:, :, 0] = compressed_layers[0]
        compressedImage[:, :, 1] = compressed_layers[1]
        compressedImage[:, :, 2] = compressed_layers[2]

        return compressedImage
