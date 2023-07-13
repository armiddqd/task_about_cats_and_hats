# Task 1 - Write a Python program to compute
# the difference between two lists

def compute_difference(first: list, second: list) -> tuple:
    right_diff = []
    left_diff = []
    for i in first:
        if i not in second:
            right_diff.append(i)

    for j in second:
        if j not in first:
            left_diff.append(j)

    return (right_diff, left_diff)


def test_compute_difference():
    result1 = compute_difference(['a', 'b', 'c', 'c', 'd'], ['c', 'd', 'e'])
    assert result1 == (['a', 'b', 'c'], ['e'])
    result2 = compute_difference([], ['c', 'd', 'e'])
    assert result2 == ([], ['c', 'd', 'e'])
    result3 = compute_difference([1, 2, 3], [4, 4, 5, 6])
    assert result3 == ([1, 2, 3], [4, 4, 5, 6])
    result3 = compute_difference([1, 2, 3], [2, 3, 4])
    assert result3 == ([1], [4])


test_compute_difference()

# Task 2 - Return indices of the two numbers
# such that they add up to target


def sum_of_two(nums: list, target: int) -> list:
    result_list = []
    list_of_indexes = []

    for index in range(len(nums)):
        for next_iter_index in range(len(nums)):
            if index != next_iter_index:
                if nums[index]+nums[next_iter_index] == target:
                    result_list.append(index)
                    result_list.append(next_iter_index)

    for number in result_list:
        if number not in list_of_indexes:
            list_of_indexes.append(number)

    return list_of_indexes


def test_sum_of_two():
    result1 = sum_of_two([2, 7, 11, 15], 9)
    assert result1 == [0, 1]
    result2 = sum_of_two([3, 2, 4], 6)
    assert result2 == [1, 2]
    result3 = sum_of_two([3, 3], 6)
    assert result3 == [0, 1]


test_sum_of_two()

# Task 3 - Return a new list that contains only
# the elements that are unique from previous


def unique_elements(arr: list) -> list:
    list_of_uniques = []

    for index_value in range(len(arr)):
        arr_for_pop = arr.copy()
        arr_for_pop.pop(index_value)
        if arr[index_value] not in arr_for_pop:
            list_of_uniques.append(arr[index_value])

    return list_of_uniques


def test_unique_elements():
    result1 = unique_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result2 = unique_elements([1, 2, 3, 4, 5])
    assert result2 == [1, 2, 3, 4, 5]
    result3 = unique_elements([1, 1, 1, 1, 1])
    assert result3 == []


test_unique_elements()

# Task 4 - List contains only the elements that appear
# an odd number of times in the list


def odd_elements(arr: list) -> list:
    list_of_odd = []
    list_of_odd_results = []

    # what was in prev version
    #
    # for value in arr:
    #     counter = 0
    #     for next_value in arr:
    #         if value == next_value:
    #             counter += 1
    #     if counter % 2 != 0:
    #         list_of_odd.append(value)

    for value in arr:
        if arr.count(value) % 2 == 1:
            list_of_odd.append(value)

    for number in list_of_odd:
        if number not in list_of_odd_results:
            list_of_odd_results.append(number)

    return list_of_odd_results


def test_odd_elements():
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5])
    assert result1 == [1, 3, 4]
    result1 = odd_elements([1, 2, 3, 2, 4, 5, 5, 6, 6, 6])
    assert result1 == [1, 3, 4, 6]


test_odd_elements()

# Task 5 - Show the second-largest element in the list


def second_largest_element(arr: list) -> int:
    unique_list = []
    copied_list = arr.copy()
    sorted_list = []

    for number in arr:
        if number not in unique_list:
            unique_list.append(number)

    if len(unique_list) > 1:
        for i in range(len(arr)):
            sorted_list.append(min(copied_list))
            copied_list.remove(min(copied_list))
        return sorted_list[-2]
    else:
        return None


def test_second_largest_element():
    result1 = second_largest_element([1, 2, 3, 2, 4, 5, 5])
    assert result1 == 5
    result2 = second_largest_element([1, 2, 3, 4, 5])
    assert result2 == 4
    result3 = second_largest_element([1, 1, 1, 1, 1])
    assert result3 == None


test_second_largest_element()

# Task 6 - Calculate average and total population for cities from this list
input_list = [('New York City', 8550405),
              ('Los Angeles', 3792621),
              ('Chicago', 2695598),
              ('Houston', 2100263),
              ('Philadelphia', 1526006),
              ('Phoenix', 1445632),
              ('San Antonio', 1327407),
              ('San Diego', 1307402),
              ('Dallas', 1197816),
              ('San Jose', 945942),
              ]


def list_sort(insert_list: list):

    # previous version
    #
    # empty_list = [i[1] for i in insert_list]
    # empty_list.sort()
    # return [y for i in empty_list for y in insert_list if i == y[1]]

    def list_element(list_with_items: list):
        return list_with_items[1]

    insert_list.sort(key=list_element)

    return insert_list


def total_population(insert_list: list):
    empty_list = [i[1] for i in insert_list]
    return sum(empty_list)


def avg_population(insert_list: list):
    return total_population(insert_list)/len(insert_list)


print('The total population is: ' + str(total_population(input_list)))
print('The average population is: ' + str(avg_population(input_list)))
