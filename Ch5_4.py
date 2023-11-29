#给定一个由 1（陆地）和0（水）组成的二维网格，用其计算岛屿的数量。
# 一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。
# 你可以假设网格的4个边均被水包围。

#输入：11110 11010 11000 00000 输出：1
def numIslands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if 0 <= row < rows and 0 <= col < cols and grid[row][col] == "1":
            grid[row][col] = "0"  #标记为已访问

            #递归访问上下左右相邻的陆地
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                num_islands += 1
                dfs(row, col)

    return num_islands

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

print(numIslands(grid))  # 输出：1
