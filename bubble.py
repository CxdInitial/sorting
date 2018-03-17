def bubble_sort(elements):
    """
     Use the simple bubble sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    for count in range(length - 1, 1, -1):
        swapped = False
        for i in range(count):
            if elements[i] > elements[i+1]:
                swapped = True
                elements[i], elements[i+1] = elements[i+1], elements[i]
        if not swapped:
            break
    return elements
