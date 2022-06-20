# 32_Number_of_Islands
from typing import List


class Solution:
    # Solution0-1 - time ilmit exceeded
    def numIslands0_1(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        land_num = 0
        land_list = []
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    land_list.append(i * n + j)

        while land_list:
            stack.append(land_list.pop(0))
            while stack:
                v = stack.pop()
                if v + 1 in land_list and (v + 1) % n != 0:
                    stack.append(v + 1)
                    land_list.remove(v + 1)
                if v - 1 in land_list and v % n != 0:
                    stack.append(v - 1)
                    land_list.remove(v - 1)
                if v + n in land_list:
                    stack.append(v + n)
                    land_list.remove(v + n)
                if v - n in land_list:
                    stack.append(v - n)
                    land_list.remove(v - n)
            land_num += 1
        return land_num

    """
    Time Limit Exceeded - 아마 remove와 in 메서드 때문에 시간이 초과 
    """

    # Solution0-2 - using DFS-iterative
    def numIslands0_2(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        land_num = 0
        stack = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    stack.append((i, j))
                    while stack:
                        v = stack.pop()
                        x, y = v[0], v[1]
                        grid[x][y] = "0"
                        if y >= 1 and grid[x][y - 1] == "1":
                            stack.append((x, y - 1))
                        if y < n - 1 and grid[x][y + 1] == "1":
                            stack.append((x, y + 1))
                        if x >= 1 and grid[x - 1][y] == "1":
                            stack.append((x - 1, y))
                        if x < m - 1 and grid[x + 1][y] == "1":
                            stack.append((x + 1, y))
                    land_num += 1
        return land_num

    # Solution1 - using DFS-recursive
    def numIslands1(self, grid: List[List[str]]) -> int:
        def dfs(i: int, j: int):
            # DFS 종료 시점
            if (
                i < 0
                or i >= len(grid)
                or j < 0
                or j >= len(grid[0])
                or grid[i][j] != "1"
            ):
                return

            grid[i][j] = "0"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)  # 해당 육지 탐색
                    count += 1
        return count


sol = Solution()
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "1"],
    ["1", "0", "0", "1", "1"],
]
print(sol.numIslands1(grid))
