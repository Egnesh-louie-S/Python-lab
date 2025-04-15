#1. Write a Python program to sum all the items in a list.
def sum_list(lst):
    total = 0
    for item in lst:
        total += item
    return total
print(sum_list([1, 2, 3, 4, 5]))
print("\n")


#2. Write a Python program to get the largest and smallest number from a list without builtin functions.

def min_max(lst):
    if not lst:
        return None, None
    smallest = lst[0]
    largest = lst[0]
    for item in lst:
        if item < smallest:
            smallest = item
        if item > largest:
            largest = item
    return smallest, largest
print(min_max([3, 5, 1, 9, -2, 4]))
print("\n")


#3. Write a Python program to find duplicate values from a list and display those.

def find_duplicates(lst):
    seen = set()
    duplicates = set()
    
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    
    return list(duplicates)
print(find_duplicates([1, 1, 2, 3, 4, 4, 5, 1]))
print("\n")


#4. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
#Original list: [1, 1, 2, 3, 4, 4, 5, 1] Length of the first part of the list: 3 Splitted the said list into two parts: ([1, 1, 2], [3, 4, 4, 5, 1])

def split_list(lst, first_part_len):
    first_part = lst[:first_part_len]
    second_part = lst[first_part_len:]
    return first_part, second_part
original_list = [1, 1, 2, 3, 4, 4, 5, 1]
length_first_part = 3
print(split_list(original_list, length_first_part))
print("\n")


#5. Write a Python program to traverse a given list in reverse order,
#and print the elements with the original index. Original list: ['red', 'green', 'white', 'black'] Traverse the said list in reverse order: black white green red

def reverse_traverse_with_index(lst):
    for i in range(len(lst) - 1, -1, -1):
        print(f"{lst[i]} (index {i})")
colors = ['red', 'green', 'white', 'black']
reverse_traverse_with_index(colors)


