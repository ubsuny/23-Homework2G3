import numpy as np

def calculate_trace(matrix):
    """
    Calculate the trace of a square matrix.

    Parameters:
    matrix (numpy.ndarray): The input square matrix.

    Returns:
    float: The trace of the matrix (sum of diagonal elements).
    """
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    trace = np.trace(matrix)
    return trace

# Unit Test
import unittest

class TestCalculateTrace(unittest.TestCase):

    def test_trace(self):
        # Test with a 3x3 identity matrix
        identity_matrix = np.identity(3)
        self.assertEqual(calculate_trace(identity_matrix), 3.0)

        # Test with a 2x2 matrix with known trace
        matrix = np.array([[1, 2], [3, 4]])
        self.assertEqual(calculate_trace(matrix), 5.0)

    def test_non_square_matrix(self):
        # Test with a non-square matrix
        non_square_matrix = np.array([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            calculate_trace(non_square_matrix)

if __name__ == "__main__":
    unittest.main()