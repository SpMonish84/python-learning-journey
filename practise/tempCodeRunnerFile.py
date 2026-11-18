matrix = [[10, 20], [30, 40], [50, 60]]
target = 30

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Target {target} found at Row: {i}, Column: {j}")