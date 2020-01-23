def lattice_paths(num_rows,num_cols):
    grid = [[int(j==0) for j in range(num_cols+1)] for _ in range(num_rows+1)]
    grid[0] = [1 for _ in range(num_cols+1)]

    for i in range(1,num_rows+1):
        for j in range(1,num_cols+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    
    return (grid[num_rows][num_cols])

if __name__ == "__main__":
    print(lattice_paths(2,2))
    print(lattice_paths(5,5))
    print(lattice_paths(20,20))