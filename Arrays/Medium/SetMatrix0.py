class better:
    
    def SetMatrix0_bruteforce(self, arr):
        if not arr or not arr[0]:
            return arr

        m, n = len(arr), len(arr[0])
        rows_mark = [False] * m
        cols_mark = [False] * n

        # First pass: record rows/cols that contain a zero
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    rows_mark[i] = True
                    cols_mark[j] = True

        # Second pass: zero out marked rows/cols
        for i in range(m):
            for j in range(n):
                if rows_mark[i] or cols_mark[j]:
                    arr[i][j] = 0

        return arr

# test
arr = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1],
]
print("markers:", better().SetMatrix0_bruteforce(arr))
# expected [[1,0,1],[0,0,0],[1,0,1]]



class BruteForceSentinel:
    def MarkRow0(self, arr, r):
        n = len(arr[0])
        for j in range(n):
            if arr[r][j] != 0:
                arr[r][j] = -1

    def MarkColumn0(self, arr, c):
        m = len(arr)
        for i in range(m):
            if arr[i][c] != 0:
                arr[i][c] = -1

    def SetMatrix0_bruteforce(self, arr):
        if not arr or not arr[0]:
            return arr

        m, n = len(arr), len(arr[0])
        zero_positions = []

        # 1) Record original zero positions
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 0:
                    zero_positions.append((i, j))

        # 2) For each original zero, mark its row and column with -1 (don't touch existing zeros)
        for (r, c) in zero_positions:
            self.MarkRow0(arr, r)
            self.MarkColumn0(arr, c)

        # 3) Convert -1 markers into 0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == -1:
                    arr[i][j] = 0

        return arr

# test
arr2 = [
    [1, 1, 1, 1],
    [1, 0, 1, 1],
    [1, 1, 1, 0],
    [1, 1, 1, 1],
]
print("sentinel:", BruteForceSentinel().SetMatrix0_bruteforce(arr2))
# expected:
# [
#  [1,0,1,0],
#  [0,0,0,0],
#  [0,0,0,0],
#  [1,0,1,0]
# ]
