# Enter your code here. Read input from STDIN. Print output to STDOUT
def abs_diff(numbers, T):
    min_grid = [[[] for y in numbers] for x in numbers]
    final = ''
    index = 0
    for i in range(T):
        for j in range(i+1,T):
            min_grid[i][j] = abs(numbers[i] - numbers[j])

    min_val = min(min(x) for x in min_grid)
    #print min_val
    
    for i in range(T):
        for j in range(i,T):
            if min_grid[i][j] == min_val:
                final = final + str(numbers[i]) + ' ' + str(numbers[j]) + ' '
    print final
    #print min_grid
    #print min_val

T = int(raw_input())
numbers = map(int, raw_input().strip().split())

abs_diff = abs_diff(numbers, T)

#print abs_diff.final