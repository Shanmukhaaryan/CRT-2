def diagonalSort(mat):
    m, n = len(mat), len(mat[0])

    for r in range(m):
        i, j = r, 0
        a = []
        while i < m and j < n:
            a.append(mat[i][j])
            i += 1
            j += 1
        a.sort()
        i, j = r, 0
        for x in a:
            mat[i][j] = x
            i += 1
            j += 1

    for c in range(1, n):
        i, j = 0, c
        a = []
        while i < m and j < n:
            a.append(mat[i][j])
            i += 1
            j += 1
        a.sort()
        i, j = 0, c
        for x in a:
            mat[i][j] = x
            i += 1
            j += 1

    return mat

if __name__ == '__main__':
    m, n = map(int, input().split())
    mat = []
    for i in range(m):
        mat.append(list(map(int, input().split())))
    print(diagonalSort(mat))