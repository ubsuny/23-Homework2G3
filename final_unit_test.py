import unittest
import numpy as np
from TraceTimeCheck import recursive_trace

class TestTraceMethods(unittest.TestCase):
    def test_recursive_trace(self):
        # Test with a 2x2 matrix
        matrix_2x2 = [[2, 1], [1, 3]]
        expected_trace_2x2 = 5
        result_2x2 = recursive_trace(matrix_2x2)
        self.assertEqual(result_2x2, expected_trace_2x2)

        # Test with a 3x3 matrix
        matrix_3x3 = [[2, 1, 1], [1, 3, 1], [1, 1, 4]]
        expected_trace_3x3 = 9
        result_3x3 = recursive_trace(matrix_3x3)
        self.assertEqual(result_3x3, expected_trace_3x3)

        # Test with an empty matrix (should raise an error)
        empty_matrix = []
        with self.assertRaises(IndexError):
            recursive_trace(empty_matrix)

        # Test with a non-square matrix (should raise an error)
        non_square_matrix = [[2, 1, 1], [1, 3, 1]]
        with self.assertRaises(ValueError):
            recursive_trace(non_square_matrix)

if __name__ == '__main__':
    unittest.main()