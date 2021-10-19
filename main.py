grid = [[0]]#maintain rectangleness, nonempty

redistribution_count = {0: {0: 0}}

def redistribute(r, c):
    assert grid[r][c] >= 4
    if r == min(grid.keys()):
        grid[r-1] = dict.fromkeys(grid[r].keys(),0)
        redistribution_count[r-1] = dict.fromkeys(grid[r].keys(),0)
    if c == min(grid[0].keys()):
        for row in grid.values():
            row[c-1]=0
        for row in redistribution_count.values():
            row[c-1]=0
    if r == max(grid.keys()):
        grid[r+1] = dict.fromkeys(grid[r].keys(),0)
        redistribution_count[r+1] = dict.fromkeys(grid[r].keys(),0)
    if c == max(grid[0].keys()):
        for row in grid.values():
            row[c+1]=0
        for row in redistribution_count.values():
            row[c+1]=0
    grid[r][c] -= 4
    grid[r - 1][c] += 1
    grid[r + 1][c] += 1
    grid[r][c + 1] += 1
    grid[r][c - 1] += 1
    redistribution_count[r][c] += 1


def prettyPrint():
    for row in range(min(grid.keys()), max(grid.keys())+1):
        values = [grid[row][col] for col in range(min(grid[0].keys()), max(grid[0].keys())+1)]
        print(" ".join(str(i) for i in values))


def redistributeSomething():
    rows = [i for i in grid.keys()]
    columns = [j for j in grid[0].keys()]
    for row in rows:
        for column in columns:
            if (grid[row][column] >= 4):
                redistribute(row, column)
                return


def redistributeBackwards():
    rows = [i for i in grid.keys()]
    columns = [j for j in grid[0].keys()]
    for row in rows:
        for column in columns:
            if (grid[row][column] >= 4):
                redistribute(row, column)
                return


grid = {0: {0: 1000}}
num_redistributions = 0
while max([max(i.values()) for i in grid.values()]) >= 4:
    redistributeSomething()
    num_redistributions += 1
prettyPrint()
