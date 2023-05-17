n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    matrix.append(input().split())

result = [[0 for j in range(n)] for i in range(m)]

for row in range(n):
    for column in range(m):
        result[column][row] = matrix[row][column]

for row in result:
    print(*row)
