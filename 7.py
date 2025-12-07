def make_matrix(size, value=0):
    if type(size) == int:
        width = height = size
    else:
        width, height = size  

    matrix = []
    for _ in range(height):
        matrix.append([value] * width)

    return matrix
