# Compare the execution time of different implementations of matrix operations using Einstein notation: Trace of an array

We use 8 methods to calculate the trace of a square matrix. We also compare the time for each method and visualized the execution time using a bar graph. 
1. Einstein Summation Notation
2. NumPy
3. List Comprehension
4. For Loop
5. While Loop
6. SymPy 
7. Recursion
8. Eigenvalues


## Trace of an array

In linear algebra, the trace of a square matrix A, denoted tr(A), is defined to be the sum of elements on the main diagonal (from the upper left to the lower right) of A. The trace is only defined for a square matrix (n × n).


## Import libraries
```python
import numpy as np
```
import a library NumPy and name it to np

NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

```python
import time
```

Import provides various time-related functions.

```python
import matplotlib as plt
```
Import a library matplotlib.pyplot and name it to plt

Matplotlib is a plotting library for the Python programming language and its numerical mathematics extension NumPy.


## Create a square matrix
```python
mat = [[2,1,1,1],[1,3,1,1],[1,1,4,1],[1,1,1,5]]
```
declear a 4 × 4 square matrix and name it as mat

```python
rows,columns = np.shape(mat)
```
save the number of rows and columns

## Calculate the trace of matrix using different method


```python
if  rows == columns:
```
check if the matrix is a square matrix

### Einstein Notation

```python
  t0 = time.time()
```
record beginning time as `t0` using `time.time()` function by returning current time in seconds since the epoch (January 1, 1970)

```python
  trace = np.einsum('ii', mat) # Calculating Trace Using EinSum
  print("Trace Using EinSum = ", trace)
```
call function `np.einsum` from `NumPy` to calculate trace using Einstein summation notation
```python
  t1 = time.time()
```
record ending time as `t1` using `time.time()` functon





### NumPy

```python
  t2 = time.time()
  trace = np.trace(mat) # Calculating Trace Using NumPy
  print("Trace Using NumPy = ", trace)
  t3 = time.time()
```


### List Comprehension
```python
  t4 = time.time()
  trace = sum(mat[i][i] for i in range(len(mat))) # Calculating Trace Using List Comprehension
  print("Trace Using List Comprehension = ", trace)
  t5 = time.time()
```


### For Loop


```python
  t6 = time.time()
  trace = 0
  for j in range(len(mat)):
    trace = trace + mat[j][j]
  print("Trace Using For Loop = ", trace)
  t7 = time.time()
```



### While Loop

```python
  t8 = time.time()
  trace = 0
  i=0

  while i < len(mat):
    trace = trace + mat[i][i]
    i=i+1

  print("Trace Using While Loop = ", trace)
  t9 = time.time()
```



### SymPy

```python
  from sympy import Matrix

  t10 = time.time()
  matrix = Matrix(mat)

  trace = matrix.trace()

  print("Trace Using SymPy = ", trace)
  t11 = time.time()
```

### Recursion

```python
  t12 = time.time()
  trace = recursive_trace(mat)
  t13 = time.time()
  print("Trace Using Recursion = ", trace)
```



### Eigenvalues

```python
  t14= time.time()
  eigenvalues, _ = np.linalg.eig(mat)
  trace = eigenvalues.sum()
  t15 = time.time()
  print("Trace Using Eigenvalues = ", trace)
```

## Bar graph
```python
  # Lists of what will be plotted
  method = ["EinSum","NumPy","List\nComprehension",
          "For Loop", "While Loop","SymPy", "Recursion", "Eigenvalues"] # List of Methods Used

  dt = [t1-t0, t3-t2, t5-t4, t7-t6, t9-t8, t11-t10, t13-t12, t15-t14] # Time it took for each method


  # Create a bar graph
  plt.figure(figsize=(9, 9))  # Optional: Set the figure size
  plt.bar(method, dt)

  # Adding labels and title
  plt.xlabel('Method')
  plt.ylabel('Time (s)')
  plt.title('Execution Time of a Program Calculating Trace of a {}x{} Matrix'.format(rows,rows))

  # Display the plot
  plt.show()
```


## Execution Time of a Program Calculating Trace of a square Matrix

![Execution Time of a Program Calculating Trace of a square Matrix](Execution%20Time.png)




- EinSum is the slowest
- SymPy is the second slowest
- NumPy, List Comprehension, For Loop, and While Loop take similar time
- Eigenvalues is the second fastest
- Recursion is the fastest

Execution time varies each time

## Unit test


We use the `unittest` module to create unit tests to verify the correctness of the `recursive_trace` function.


```python
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
```
The TestTraceMethods class contains three test methods:

- Test square matrix: This method tests one 2 × 2 matrix and one 3 × 3 matrix, with a known trace value. It use `self.assertEqual` to check if the calculated value matches the expected value. 
- Test empty matrix: This method tests one empty matrix by using `self.assertEqual` to check id a `IndexError` is raised as expected.
- Test non square matrix: This method tests one non square matrix by using `self.assertEqual` to check id a `ValueError` is raised as expected.

### Output

For the above unit tests, we got the following outputs:
- For the  2 × 2 square matrix, Tr(matrix_2x2)=5
- For the  3 × 3 square matrix, Tr(matrix_3x3)=9
- For the empty matrix, it returns `ValueError`
- For the non square matrix, it returns `ValueError`


## Reference
ChatGPT
https://en.wikipedia.org/wiki/Trace_(linear_algebra)
https://docs.python.org/3/library/time.html

