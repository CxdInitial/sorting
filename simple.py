def insert_sort(elements):
    """
    Use the simple insertion sort algorithm to sort the :param elements.
    :param elements: must be a sequence which has the function __get_item__ and __len__.
    :return: the sorted elements
    """
    if not len(elements) or len(elements) == 1:
        return elements
    for index in range(1, len(elements)):
        insert = elements[index]
        for position in enumerate(elements[:index+1]):
            if position[1] > insert:
                break
        for i in range(index, position[0], -1):
            elements[i] = elements[i-1]
        elements[position[0]] = insert
        print(insert, position, elements)
    return elements
