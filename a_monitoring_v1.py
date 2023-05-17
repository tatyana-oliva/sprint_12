n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    row = input()
    row = row.split()
    row = [int(v) for v in row]
    matrix.append(row)

# print(matrix)
result = [0] * m
for i in range(m):
    result[i] = [0] * n

for row in range(n):
    for column in range(row, m):
        if row == column:
            result[row][column] = matrix[row][column]
            continue

        result[row][column] = matrix[column][row]
        result[column][row] = matrix[row][column]

if n > m:
    for row in range(m, n):
        for column in range(m):
            value = matrix[row][column]
            result[column][row] = value

for row in result:
    print(*row)
