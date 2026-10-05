def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    result = []

    det = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1] 
    if det == 0 :
        return None

    for i in range(2):
        vector = []
        for j in range(2):
            row = i
            col = j
            if( i == j):
                row = (i+1)%2
                col = (j+1)%2
            if(i + j) % 2 != 0:
                vector.append(-matrix[row][col] / det)
            else:
                vector.append(matrix[row][col] / det)
        result.append(vector)
    # result = result / det

    return result
    pass