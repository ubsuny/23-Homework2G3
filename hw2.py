def trace(A):
    # Get the number of rows in the matrix A
    row = len(A)

    # Check if the matrix is square (all rows have the same length)
    for i in A:
        if len(i) != row:
            return ('not a square matrix')  # Return a message if it's not square

    # Initialize the trace to zero
    trace = 0

    # Initialize a variable i to iterate through the matrix
    i = 0

    # Calculate the trace by summing the diagonal elements
    while i < len(A):
        trace += A[i][i]  # Add the element at the current diagonal position to the trace
        i += 1

    return trace  # Return the calculated trace

# Test cases
A = [[1, 2, 3], [3, 4, 5], [1, 2, 3]]
B = [[1, 2], [4, 5, 6]]  # This is not a square matrix
C = [[2, 3], [4, 5]]
print(trace([[2, 3], [4, 9]]))  # Test the trace function with a 2x2 matrix

