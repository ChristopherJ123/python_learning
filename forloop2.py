numbers = [5, 2, 5, 2, 2]

# Solution 1
for x in numbers:
    print('x' * x)

print()

# Solution 2
for x in numbers:
    for y in range(x):
        print('x', end='')
    print()

print()

# Solution 3
for x in numbers:
    output = ''
    for y in range(x):
        output += 'x'
    print(output)
