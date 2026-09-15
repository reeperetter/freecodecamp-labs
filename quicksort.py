def quick_sort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    pivot = array[0]
    less = []
    equal = []
    greater = []
    for i in array:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            greater.append(i)
        else:
            equal.append(i)
    less = quick_sort(less)
    greater = quick_sort(greater)
    result = less + equal + greater

    return result
