def insertion_sort(list):
    # Iterate through the list, starting at the second element
    # (the first element is already considered sorted)
    for i in range(1, len(list)):
        print(list)
        # Save the current value in a variable
        current_value = list[i]
        # Save the index of the current element
        current_position = i
        # Iterate through the sorted portion of the list
        # (the portion to the left of the current element)
        # and shift the elements to the right until the
        # correct position for the current element is found
        while current_position > 0 and list[current_position - 1] > current_value:
            list[current_position] = list[current_position - 1]
            current_position = current_position - 1
        # Insert the current element in the correct position
        list[current_position] = current_value


# Test the function with a sample list
sample_list = [5, 2, 4, 6, 1, 3]
insertion_sort(sample_list)
print(sample_list)  # prints [1, 2, 3, 4, 5, 6]
