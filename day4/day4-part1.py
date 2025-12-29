def can_access_roll(grid, i, j):
    num_neighbours = 0
    neighbours = [(i-1, j), (i-1, j-1), (i-1, j+1), (i+1, j), (i+1, j-1),(i+1, j+1), (i, j-1), (i, j+1)]

    for di, dj in neighbours:
        if 0 <= di < len(grid) and 0 <= dj < len(grid[0]) and grid[di][dj] == '@':
            num_neighbours += 1
    return num_neighbours < 4

def main():
    num_accessible_rolls = 0
    
    with open('day4-input.txt', 'r') as file:
        matrix = [[char for char in line.strip()] for line in file]
        rows, cols = len(matrix), len(matrix[0])
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '@' and can_access_roll(matrix, i, j):
                    num_accessible_rolls += 1
    
    print("Number of Accessible Rolls: ", num_accessible_rolls)

if __name__ == "__main__":
    main()
