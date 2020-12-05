def maxpooling_2x2(image, mask):
    M, N = image.shape

    K = 2
    L = 2

    MK = M // K
    NL = N // L

    image = image[:MK * 2, :NL * 2].reshape(MK, 2, NL, 2).max(axis=(1, 3))
    image = image.flatten()
    res = image @ mask
    return res
