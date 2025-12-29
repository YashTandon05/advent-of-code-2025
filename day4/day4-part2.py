import copy

def can_access_roll(grid_og, grid_edited, i, j):
    num_neighbours = 0
    neighbours = [(i-1, j), (i-1, j-1), (i-1, j+1), (i+1, j), (i+1, j-1),(i+1, j+1), (i, j-1), (i, j+1)]

    for di, dj in neighbours:
        if 0 <= di < len(grid_og) and 0 <= dj < len(grid_og[0]) and grid_og[di][dj] == '@':
            num_neighbours += 1
    if num_neighbours < 4:
        grid_edited[i][j] = 'x'
        return True
    return False

def main():
    num_accessible_rolls = 0
    
    with open('day4-input.txt', 'r') as file:
        matrix_og = [[char for char in line.strip()] for line in file]
        matrix_edited = copy.deepcopy(matrix_og)
        rows, cols = len(matrix_og), len(matrix_og[0])
        while True:
            curr_accessible_rolls = 0
            for i in range(rows):
                for j in range(cols):
                    if matrix_og[i][j] == '@':
                        if can_access_roll(matrix_og, matrix_edited, i, j):
                            curr_accessible_rolls += 1

            matrix_og = copy.deepcopy(matrix_edited)
            num_accessible_rolls += curr_accessible_rolls
            if curr_accessible_rolls == 0: break
    
    print("Number of Accessible Rolls: ", num_accessible_rolls)

if __name__ == "__main__":
    main()
