def bubble_sort(array_bubble_sort):
    for i in range(len(array_bubble_sort)):
        for j in range(len(array_bubble_sort)-i - 1):
            if array_bubble_sort[j] > array_bubble_sort[j+1]:
                temp = array_bubble_sort[j]
                array_bubble_sort[j] = array_bubble_sort[j+1]
                array_bubble_sort[j+1] = temp


def print_array(array_print):
    answer = ""
    for i in range(len(array_print)):
        answer += f"{array_print[i]} "
    print("\nBubble sorted = " + answer)


print("Welcome to Bubble Sort")
print("Enter length")
length = int(input())
array_input = [int(input(f"Index of {x} = ")) for x in range(length)]

bubble_sort(array_input)
print_array(array_input)
