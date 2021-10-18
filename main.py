grid = [[0]]#maintain rectangleness, nonempty

redistribution_count = [[0]]

def redistribute(r, c):
    assert grid[r][c] >= 4
    if r == 0:
        grid.insert(0, [0] * len(grid[0]))
        redistribution_count.insert(0, [0] * len(grid[0]))
        r += 1
    if c == 0:
        for row in grid:
            row.insert(0, 0)
        for row in redistribution_count:
            row.insert(0, 0)
        c += 1
    if r == len(grid) - 1:
        grid.append([0] * len(grid[0]))
        redistribution_count.append([0] * len(grid[0]))
    if c == len(grid[0]) - 1:
        for row in grid:
            row.append(0)
        for row in redistribution_count:
            row.append(0)
    grid[r][c] -= 4
    grid[r - 1][c] += 1
    grid[r + 1][c] += 1
    grid[r][c + 1] += 1
    grid[r][c - 1] += 1
    redistribution_count[r][c] += 1


def prettyPrint():
    for row in grid:
        print(" ".join(str(i) for i in row))


def redistributeSomething():
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if (grid[row][column] >= 4):
                redistribute(row, column)
                return


def redistributeBackwards():
    for row in range(len(grid)):
        row = len(grid) - row - 1
        for column in range(len(grid[row])):
            column = len(grid[row]) - column - 1
            if (grid[row][column] >= 4):
                redistribute(row, column)


grid = [[1000]]
num_redistributions = 0
while max([max(i) for i in grid]) >= 4:
    redistributeSomething()
    num_redistributions += 1
    if(num_redistributions % 100 == 0):
        prettyPrint()
        print("---------")
grid = redistribution_count
prettyPrint()
