#Compare the execution time of different implementations of matrix operations using Einstein notation: Trace of an array

We use 6 methods to calculate the trace of a square matrix. We also compare the time for each method and visualized the execution time using a bar graph. 
1. Einstein Notation
2. NumPy
3. List Comprehension
4. For Loop
5. While Loop
6. SymPy 
 

##Trace of an array

In linear algebra, the trace of a square matrix A, denoted tr(A), is defined to be the sum of elements on the main diagonal (from the upper left to the lower right) of A. The trace is only defined for a square matrix (n × n).


##Import libraries
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


##Creat a square matrix
```python
mat = [[2,1,1,1],[1,3,1,1],[1,1,4,1],[1,1,1,5]]
```
declear a 4 × 4 square matrix and name it as mat

```python
rows,columns = np.shape(mat)
```
Save the number of rows and columns

##Calculate the trace of matrix using different method


###Einstein Notation

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





###NumPy

```python
  t2 = time.time()
  trace = np.trace(mat) # Calculating Trace Using NumPy
  print("Trace Using NumPy = ", trace)
  t3 = time.time()
```


###List Comprehension
```python
  t4 = time.time()
  trace = sum(mat[i][i] for i in range(len(mat))) # Calculating Trace Using List Comprehension
  print("Trace Using List Comprehension = ", trace)
  t5 = time.time()
```


###For Loop


```python
  t6 = time.time()
  trace = 0
  for j in range(len(mat)):
    trace = trace + mat[j][j]
  print("Trace Using For Loop = ", trace)
  t7 = time.time()
```



###While Loop

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



###SymPy

```python
  from sympy import Matrix

  t10 = time.time()
  matrix = Matrix(mat)

  trace = matrix.trace()

  print("Trace Using SymPy = ", trace)
  t11 = time.time()
```




##Unit test


##Reference
Wikipedia
https://en.wikipedia.org/wiki/Trace_(linear_algebra)
