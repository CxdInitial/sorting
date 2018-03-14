def insert_sort(elements):
    """
    Use the simple insertion sort algorithm to sort the :param elements.
    :param elements: must be a sequence which has the function __get_item__ and __len__.
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
        print(insert, position, elements)
    return elements
