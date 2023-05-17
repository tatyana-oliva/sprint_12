n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(v) for v in input().split()])

for column in range(m):
    for row in range(n):
        print(matrix[row][column], end=' ')
    print()
