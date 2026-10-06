from typing import List

def spiralMatrixIII(rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
    ans = [[rStart, cStart]]
    r, c = rStart, cStart
    step = 1

    while len(ans) < rows * cols:
        for _ in range(step):
            c += 1
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        for _ in range(step):
            r += 1
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        step += 1

        for _ in range(step):
            c -= 1
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        for _ in range(step):
            r -= 1
            if 0 <= r < rows and 0 <= c < cols:
                ans.append([r, c])

        step += 1

    return ans


if __name__ == '__main__':
    rows, cols, rStart, cStart = map(int, input().split())
    print(spiralMatrixIII(rows, cols, rStart, cStart))