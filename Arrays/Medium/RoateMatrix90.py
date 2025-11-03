# Optimal
def rotate(matrix):
    n = len(matrix)
    # transposing the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # reversing each row of the matrix
    for i in range(n):
        matrix[i].reverse()


# Brute Force 
def rotate(matrix):
    n = len(matrix)
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - i - 1] = matrix[i][j]
    return rotated

if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotated = rotate(arr)
    print("Rotated Image")
    for i in range(len(rotated)):
        for j in range(len(rotated[0])):
            print(rotated[i][j], end=" ")
        print()

