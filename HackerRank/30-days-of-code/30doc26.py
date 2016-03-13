# Enter your code here. Read input from STDIN. Print output to STDOUT
date1 = map(int, raw_input().strip().split())
date2 = map(int, raw_input().strip().split())

if date1[0] <= date2[0] and date1[1] <= date2[1] and date1[2] <= date2[2]:
    print 0
elif date1[1] == date2[1] and date1[2] == date2[2]:
    print 15 * (date1[0] - date2[0])
elif date1[2] == date2[2]:
    print 500 * (date1[1] - date2[1])
else:
    print 10000