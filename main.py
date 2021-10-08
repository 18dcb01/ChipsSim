grid = [[4,0],[0,4]]#maintain rectangleness, nonempty

def redistribute(r,c):
    assert grid[r][c] >= 4
    grid[r][c] -= 4
    if r == 0:
        grid.insert(0,[0]*len(grid[0]))
        r += 1
    if c == 0:
        for row in grid:
            row.insert(0,0)
        c += 1
    if r == len(grid)-1:
        grid.append([0]*len(grid[0]))
    if c == len(grid[0])-1:
        for row in grid:
            row.append(0)
    grid[r-1][c] += 1
    grid[r+1][c] += 1
    grid[r][c+1] += 1
    grid[r][c-1] += 1
    
def prettyPrint():
    for row in grid:
        print(" ".join(str(i) for i in row))
        
prettyPrint()
print("becomes")
redistribute(0,0)
redistribute(2,2)

prettyPrint()
