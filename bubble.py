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
            if elements[i] > elements[i + 1]:
                swapped = True
                elements[i], elements[i + 1] = elements[i + 1], elements[i]
        if not swapped:
            break
    return elements


# Used for shell sorting(from https://oeis.org/A003586)
gaps = [1, 2, 3, 4, 6, 8, 9, 12, 16, 18, 24, 27, 32, 36, 48, 54, 64, 72, 81, 96, 108, 128, 144, 162, 192, 216, 243,
        256, 288, 324, 384, 432, 486, 512, 576, 648, 729, 768, 864, 972, 1024, 1152, 1296, 1458, 1536, 1728, 1944,
        2048, 2187, 2304, 2592, 2916, 3072, 3456, 3888]


def shell_sort(elements):
    """
    Use the simple shell sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    i = 0
    for i in range(len(gaps)):
        if gaps[i] >= len(elements):
            break
    for gap in range(i - 1, -1, -1):
        gap = gaps[gap]
        index = gap
        while index < length:
            i = 0
            while elements[i] < elements[index]:
                i += gap
            insert = elements[index]
            if i < index:
                j = index
                while j >= gap + i:
                    elements[j] = elements[j - gap]
                    j -= gap
                elements[i] = insert
            index += gap
    return elements


def comb_sort(elements):
    """
    Use the simple comb sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    copy = length - 1
    steps = []
    while copy > 1:
        if copy == 9 or copy == 10:
            copy = 11
        steps.append(copy)
        copy = int(copy / 1.3)
    steps.append(1)
    if length == 10 or length == 11:
        steps = steps[1:]
    for step in range(len(steps)):
        step = steps[step]
        if step > length / 2:
            if elements[0] > elements[0 + step]:
                elements[0], elements[0 + step] = elements[0 + step], elements[0]
        else:
            limit = length
            while limit > step:
                i = 0
                while i + step < limit:
                    if elements[i] > elements[i + step]:
                        elements[i], elements[i + step] = elements[i + step], elements[i]
                    i += step
                limit -= step
    return elements
