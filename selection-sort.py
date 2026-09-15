def selection_sort(array: list[int]) -> list[int] | None:
    last_minimum_element_index = 0
    current_index = 1

    while last_minimum_element_index < len(array) - 1:
        minimum_index = last_minimum_element_index
        minimum = array[minimum_index]

        for _ in array[last_minimum_element_index + 1:]:
            if array[current_index] < minimum:
                minimum = array[current_index]
                minimum_index = current_index
            current_index += 1

        if minimum_index != last_minimum_element_index:
            array[minimum_index], array[last_minimum_element_index] = array[last_minimum_element_index], array[minimum_index]

        last_minimum_element_index += 1
        current_index = last_minimum_element_index + 1

    return array