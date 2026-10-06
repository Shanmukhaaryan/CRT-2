from typing import List

def setZeroes(matrix: List[List[int]]) -> List[List[int]]:
    r = {i for i in range(len(matrix)) if 0 in matrix[i]}
    c = {j for j in range(len(matrix[0])) if any(matrix[i][j] == 0 for i in range(len(matrix)))}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in r or j in c:
                matrix[i][j] = 0
    return matrix

if __name__ == '__main__':
    matrix = []
    while True:
        line = input()
        if not line.strip():
            break
        matrix.append(list(map(int, line.split())))
    print(setZeroes(matrix))