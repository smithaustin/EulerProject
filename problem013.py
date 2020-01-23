def sum_large_values(path):
    vals = [int(line.strip()) for line in open(path, 'r')]
    return sum(vals)

if __name__ == "__main__":
    print(sum_large_values('inputs/problem013.txt'))