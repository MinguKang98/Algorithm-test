# 2580_스도쿠

import sys


def sudoku(i):
    if i == 9:
        print("\n".join(" ".join(arr[i]) for i in range(9)))
    else:
        for j in range(1,10):
            if j not in arr[i]:


if __name__ == "__main__":
    arr = [sys.stdin.readline().split() for _ in range(9)]
    sudoku(0)
