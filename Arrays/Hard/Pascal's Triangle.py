def Pascals_BruteFroce(numRows):
    triangle = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

def pascals_best(N):
    row = []
    val = 1
    row.append(val)
    for k in range(1, N):
        val = val * (N - k) // k
        row.append(val)
    
    return row

def pascals_optimal(r,c):
        n = r - 1
        k = c - 1

        result = 1

        # Compute C(n, k) using iterative formula
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)

        return result

print(pascals_optimal(5,3))
print(pascals_best(5))


