def selection_sort(numbers):

    for i in range(len(numbers)):
        min_pos = i
        for j in range(i, len(numbers)):
            if(numbers[j] < numbers[min_pos]):
                min_pos = j
        numbers[i], numbers[min_pos] = numbers[min_pos], numbers[i]


numbers = [34, 78, 56, 12, 98, 46]

selection_sort(numbers)
print(numbers)
