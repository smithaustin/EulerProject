def max_path_triangle_sum(path):
    tri = [[int(x) for x in line.split()] for line in open(path, 'r')]
    return (max(biggest_sums_given_end(len(tri)-1, tri)))

def biggest_sums_given_end(end_line_idx, tri):
    if end_line_idx == 0:
        return tri[0]
    
    sums_last_line = biggest_sums_given_end(end_line_idx-1, tri)
    current_line = tri[end_line_idx]
    sums_current_line = []

    for i in range(len(current_line)):
        if i == 0 :
            sums_current_line.append(sums_last_line[0] + current_line[i])
        elif i == len(sums_last_line):
            sums_current_line.append(sums_last_line[-1] + current_line[i])
        else:
            sums_current_line.append(max(sums_last_line[i-1], sums_last_line[i]) + current_line[i])

    return sums_current_line

if __name__ == "__main__":
    print(max_path_triangle_sum('inputs/problem018.txt'))
    print(max_path_triangle_sum('inputs/p067_triangle.txt'))