def diagonalDifference(arr):
    n = len(arr)
    return abs(sum(arr[i][i] - arr[i][n-1-i] for i in range(n)))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)