# This file will include the case unit tests for trace time check using various methods.
import unittest
import numpy as np
from sympy import Matrix
import time

mat = [[2, 1, 1], [1, 3, 1], [1, 1, 4]]

class TestTraceMethods(unittest.TestCase):
    def test_einsum(self):
        t0 = time.time()
        trace = np.einsum('ii', mat)
        t1 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)  # Expected trace for this matrix is 9.
        print("Trace Using EinSum Time:", t1 - t0)

    def test_numpy(self):
        t2 = time.time()
        trace = np.trace(mat)
        t3 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using NumPy Time:", t3 - t2)

    def test_list_comprehension(self):
        t4 = time.time()
        trace = sum(mat[i][i] for i in range(len(mat)))
        t5 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using List Comprehension Time:", t5 - t4)

    def test_for_loop(self):
        t6 = time.time()
        trace = 0
        for j in range(len(mat)):
            trace = trace + mat[j][j]
        t7 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using For Loop Time:", t7 - t6)

    def test_while_loop(self):
        t8 = time.time()
        trace = 0
        i = 0
        while i < len(mat):
            trace = trace + mat[i][i]
            i = i + 1
        t9 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using While Loop Time:", t9 - t8)

    def test_sympy(self):
        t10 = time.time()
        matrix = Matrix(mat)
        trace = matrix.trace()
        t11 = time.time()
        self.assertAlmostEqual(trace, 9, places=6)
        print("Trace Using SymPy Time:", t11 - t10)

if __name__ == '__main__':
    unittest.main()
