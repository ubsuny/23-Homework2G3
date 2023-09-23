import unittest
import numpy as np
from sympy import Matrix
import time

# Define a function to calculate the trace using the given algorithm
def calculate_trace(matrix):
    t0 = time.time()
    trace = np.einsum('ii', matrix)
    t1 = time.time()
    return trace, t1 - t0

class TestTraceMethods(unittest.TestCase):
    def test_10x10_matrix(self):
        # Create a 10x10 matrix with random values
        mat = np.random.randint(1, 10, (10, 10))
        
        # Calculate the trace using the provided algorithm
        trace, execution_time = calculate_trace(mat)

        # Calculate the trace using NumPy for comparison
        trace_numpy = np.trace(mat)

        # Check if the calculated trace matches the trace calculated using NumPy
        self.assertAlmostEqual(trace, trace_numpy, places=6)
        print("Trace Using Provided Algorithm for 10x10 Matrix Time:", execution_time)

    def test_100x100_matrix(self):
        # Create a 100x100 matrix with random values
        mat = np.random.randint(1, 10, (100, 100))
        
        # Calculate the trace using the provided algorithm
        trace, execution_time = calculate_trace(mat)

        # Calculate the trace using NumPy for comparison
        trace_numpy = np.trace(mat)

        # Check if the calculated trace matches the trace calculated using NumPy
        self.assertAlmostEqual(trace, trace_numpy, places=6)
        print("Trace Using Provided Algorithm for 100x100 Matrix Time:", execution_time)

    def test_500x500_matrix(self):
        # Create a 500x500 matrix with random values
        mat = np.random.randint(1, 10, (500, 500))
        
        # Calculate the trace using the provided algorithm
        trace, execution_time = calculate_trace(mat)

        # Calculate the trace using NumPy for comparison
        trace_numpy = np.trace(mat)

        # Check if the calculated trace matches the trace calculated using NumPy
        self.assertAlmostEqual(trace, trace_numpy, places=6)
        print("Trace Using Provided Algorithm for 500x500 Matrix Time:", execution_time)

if __name__ == '__main__':
    unittest.main()
