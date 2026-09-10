# A matrix is a rectangular arrangement of values organized into rows and columns.
# A = [[1 2 3],
#      [4 5 6]]
# 2 rows, 3 columns, so dimension 2x3
# indexing starts from zero
# A[0][0] - row 0 and column 1

# Dimension = row X column

# Matrix elements - Each individual value in a matrix is called an element
# row and column access = A[row][column]

# The Matrix Multiplication Rule
# (m x n)(n x p) = (m x p)
# The middle numbers must be equal.


# Matrix Multiplication vs Element-Wise Multiplication
A = [[1,2],
    [3,4]]
B = [[5,6],
    [7,8]]
# = 1x5 , 2x6
# = 3x7 , 4x8
C = [[5,12],
    [21,32]]
# element wise calculation - same position × same position

# = [1x5+2x7 , 1x6+2x8]
#   [3x5+4x7 , 3x6+4x8]
C = [[19,22],
    [43,50]]
# matrix multiplication - row × column → multiply → add

# * vs @ in Python
# *  → element-wise multiplication
# @  → matrix multiplication
# A * B = element wise multiplication
# A @ B = matrix multiplication

# 1. Matrix
#    → rows + columns
# 2. Dimension
#    → rows × columns
# 3. Matrix multiplication rule
#    → inner dimensions must match
# 4. Individual result element
#    → row × column → multiply → add
# 5. Manual implementation
#    → three nested loops + accumulator



# A = [[1,2,3],[4,5,6]]

# for i in range(len(A)) :
#     for j in range(len(A[i])):
#         print(A[i][j])
