# could be made faster by makine a lookup table of the next step
# instead of recalculating the values each time ad appending them to a list

def longest_collatz_chain(maximum):
    longest_collatz = (0,0, [])
    for start in range(1,maximum):
        collatz_chain = [start]
        while collatz_chain[-1] != 1:
            if collatz_chain[-1]%2 ==0:
                collatz_chain.append(int(collatz_chain[-1]/2))
            else:
                collatz_chain.append(3*collatz_chain[-1] + 1)
            # print(collatz_chain)
        if longest_collatz[1] < len(collatz_chain):
            longest_collatz = (start, len(collatz_chain), collatz_chain)
    
    return longest_collatz
    


if __name__ == "__main__":
    print(longest_collatz_chain(14))
    print(longest_collatz_chain(100))
    print(longest_collatz_chain(1000000))