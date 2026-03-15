import numpy as np
import math

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    dot = 0
    for i in range(len(a)):
        dot += a[i] * b[i]

    sum_square_a = 0
    sum_square_b = 0
    for i in range(len(a)):
        sum_square_a += a[i] * a[i]
    for j in range(len(b)):
        sum_square_b += b[j] * b[j]
    Norm = math.sqrt(sum_square_a) * math.sqrt(sum_square_b)
    if Norm == 0:
        return 0
    return dot/Norm
        