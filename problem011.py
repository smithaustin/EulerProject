def largest_product_in_square(path):
    """Returns the largest prodcut of length 4 in any direction of a integer square"""
    square = [[int(x) for x in line.split()] for line in open(path, 'r')]
    
    largest_prod = 1
    large_idx = (-1, -1)
    # Horizontal Prod
    for (i,row) in enumerate(square):
        j = 0
        while j < len(row)-4:
            current_prod = row[j]*row[j+1]*row[j+2]*row[j+3]
            largest_prod = max(largest_prod, current_prod)
            if current_prod == largest_prod:
                large_idx = (i,j)
            j += 1
    
    #Vertical Prod
    for (i,row) in enumerate(square[0:16]):
        for (j,col) in enumerate(row):
            current_prod = square[i][j]*square[i+1][j]*square[i+2][j]*square[i+3][j]
            largest_prod = max(largest_prod, current_prod)
            if current_prod == largest_prod:
                large_idx = (i,j)

    #Diagonal like this \
    for (i,row) in enumerate(square[0:16]):
        for (j,col) in enumerate(row[0:16]):
            current_prod = square[i][j]*square[i+1][j+1]*square[i+2][j+2]*square[i+3][j+3]
            largest_prod = max(largest_prod, current_prod)
            if current_prod == largest_prod:
                large_idx = (i,j)
    
    #Diagonal like this /
    for (i,row) in enumerate(square[0:16]):
        for (j,col) in enumerate(row[3:]):
            current_prod = square[i][j]*square[i+1][j-1]*square[i+2][j-2]*square[i+3][j-3]
            largest_prod = max(largest_prod, current_prod)
            if current_prod == largest_prod:
                large_idx = (i,j)

    return (largest_prod, large_idx)

if __name__ == "__main__":
    print(largest_product_in_square('inputs/problem011.txt'))