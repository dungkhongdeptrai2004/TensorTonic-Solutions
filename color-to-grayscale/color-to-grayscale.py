def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    
    N = len(image)
    M = len(image[0])
    out_image = []
    for i in range(N):
        add = [0 for j in range(M)]
        out_image.append(add)

    for i in range(N):
        for j in range(M):
            out_image[i][j] = image[i][j][0] * 0.299 + image[i][j][1] * 0.587 + image[i][j][2] * 0.114
    return out_image