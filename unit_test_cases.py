import unittest
import numpy as np
from sympy import Matrix
import time

class TestTraceMethods(unittest.TestCase):
    def test_2x2_matrix(self):
        mat = [[2, 1], [1, 3]]
        t0 = time.time()
        trace = np.einsum('ii', mat)
        t1 = time.time()
        self.assertAlmostEqual(trace, 5, places=6)
        print("Trace Using EinSum for 2x2 matrix Time:", t1 - t0)

        t2 = time.time()
        trace = np.trace(mat)
        t3 = time.time()
        self.assertAlmostEqual(trace, 5, places=6)
        print("Trace Using NumPy for 2x2 matrix Time:", t3 - t2)

        t10 = time.time()
        matrix = Matrix(mat)
        trace = matrix.trace()
        t11 = time.time()
        self.assertAlmostEqual(trace, 5, places=6)
        print("Trace Using SymPy for 2x2 matrix Time:", t11 - t10)

    def test_3x3_matrix(self):
        mat = [[2, 1, 1], [1, 3, 1], [1, 1, 4]]
        t0 = time.time()
        trace = np.einsum('ii', mat)
        t1 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using EinSum for 3x3 matrix Time:", t1 - t0)

        t2 = time.time()
        trace = np.trace(mat)
        t3 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using NumPy for 3x3 matrix Time:", t3 - t2)

        t10 = time.time()
        matrix = Matrix(mat)
        trace = matrix.trace()
        t11 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using SymPy for 3x3 matrix Time:", t11 - t10)

    def test_2x3_matrix(self):
        mat = [[2, 1, 3], [1, 3, 2]]
        t0 = time.time()
        # EinSum and NumPy do not work for non-square matrices
        with self.assertRaises(ValueError):
            np.einsum('ii', mat)
            np.trace(mat)

        t10 = time.time()
        # SymPy can handle non-square matrices
        matrix = Matrix(mat)
        trace = matrix.trace()
        t11 = time.time()
        self.assertAlmostEqual(trace, 5, places=6)
        print("Trace Using SymPy for 2x3 matrix Time:", t11 - t10)

if __name__ == '__main__':
    unittest.main()
