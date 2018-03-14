def insert_sort(elements):
    """
    Use the simple insertion sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    if not len(elements) or len(elements) == 1:
        return elements
    for index in range(1, len(elements)):
        insert = elements[index]
        for position in range(0, index+1):
            if elements[position] > insert:
                break
        for i in range(index, position, -1):
            elements[i] = elements[i-1]
        elements[position] = insert
    return elements


def select_sort(elements):
    """
    Use the simple selection sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    if not len(elements) or len(elements) == 1:
        return elements
    for sorted_count in range(0, len(elements)-1):
        min_index = sorted_count
        for index in range(sorted_count, len(elements)):
            if elements[index] < elements[min_index]:
                min_index = index
        elements[sorted_count], elements[min_index] = elements[min_index], elements[sorted_count]
    return elements
