# Calculate Trace of a Square Matrix

In this Python example, we will define a function to calculate the trace of a square matrix using the NumPy library. The trace of a matrix is the sum of its diagonal elements.

## Function: calculate_trace(matrix)

```python
import numpy as np

def calculate_trace(matrix):
    """
    Calculate the trace of a square matrix.

    Parameters:
    matrix (numpy.ndarray): The input square matrix.

    Returns:
    float: The trace of the matrix (sum of diagonal elements).

    Raises:
    ValueError: If the input matrix is not square (number of rows != number of columns).
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    trace = np.trace(matrix)
    return trace
