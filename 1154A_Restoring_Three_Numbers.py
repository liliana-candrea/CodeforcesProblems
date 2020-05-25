randoms = input().split(' ')
sums = list(map(int, randoms))
sums.sort()

a = sums[3] - sums[2]
b = sums[3] - sums[1]
c = sums[3] - sums[0]

print(a, b, c)
