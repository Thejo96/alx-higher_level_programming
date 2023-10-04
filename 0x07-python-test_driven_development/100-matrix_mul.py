#!/usr/bin/python3
""" matrix_mul function
"""

'''
File_name: 100-matrix_mul.py
Created: 1st of June, 2023
Auth: David James Taiye (Official0mega)
Size: undefined
Project: 0x07-python-test_driven_development
Status: submitted.
'''

def matrix_mul(m_a, m_b):
    # Validate m_a and m_b
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list, and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists, and m_b must be a list of lists")
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty, and m_b can't be empty")
    
    # Check if all elements in m_a and m_b are integers or floats
    for row in m_a + m_b:
        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("m_a should contain only integers or floats, and m_b should contain only integers or floats")
    
    # Check if all rows in m_a and m_b have the same size
    a_row_sizes = set(len(row) for row in m_a)
    b_row_sizes = set(len(row) for row in m_b)
    if len(a_row_sizes) > 1 or len(b_row_sizes) > 1:
        raise ValueError("Each row of m_a must be of the same size, and each row of m_b must be of the same size")
    
    # Check if the matrices can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            cell_value = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_a[i])))
            row.append(cell_value)
        result.append(row)
    
    return result
