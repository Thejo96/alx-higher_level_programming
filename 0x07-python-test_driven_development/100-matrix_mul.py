#!/usr/bin/python3
"""
matrix_mul function
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices.
    Args:
        m_a (list): First matrix as a list of lists.
        m_b (list): Second matrix as a list of lists.
    Returns:
        list: The result of the matrix multiplication.
    Raises:
        ValueError: If matrices are not properly formatted for multiplication.
    """

    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Both matrices must be lists of lists")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise ValueError("Both matrices must be lists of lists")

    if len(m_a) == 0 or len(m_b) == 0 or any(len(row) == 0 for row in m_a) or any(len(row) == 0 for row in m_b):
        raise ValueError("Both matrices must be non-empty")

    num_columns_a = len(m_a[0])
    num_rows_b = len(m_b)

    if any(len(row) != num_columns_a for row in m_a) or any(len(row) != num_rows_b for row in m_b):
        raise ValueError("Matrices must be of compatible sizes for multiplication")

    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result
