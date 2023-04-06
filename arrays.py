names = ['John', 'Petra', 'Athena', 'Billy']
numbers = [7, 600, 6, 700]
total_number = 0

for x in numbers:
    total_number += x

print(total_number)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)
    for item in row:
        print(item)

length = 5
z = []
for x in range(5):
    y = int(input())
    z.append(y)

print(z)
