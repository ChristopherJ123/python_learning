numbers = [1, 1, 3, 3, 5, 5, 7, 7, 9, 1, 9, 9, 9, 9, 9, 8]
# for number in numbers:
#     num_check = numbers.count(number)
#     for x in range(num_check):
#         if x > 0:
#             numbers.remove(number)
#
# numbers.sort()
# print(numbers)

unique_numbers = []
# for number in numbers:
#     if unique_numbers.count(number) < 1:
#         unique_numbers.append(number)

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)

if 1 in unique_numbers:
    print('true')

unique_numbers2 = unique_numbers.copy()

if unique_numbers is unique_numbers2:
    print('true')
else:
    print('false')
    print(unique_numbers)
    print(unique_numbers2)

