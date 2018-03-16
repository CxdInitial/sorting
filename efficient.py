def heap_sort(elements):
    """
    Use the simple heap sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    for offset in range(0, length - 1):
        origin_parent = (length - offset - 2) / 2
        if origin_parent >= 0:
            left = origin_parent * 2 + 1 + offset
            right = left + 1
            parent = origin_parent + offset
            if right >= length:
                if elements[parent] > elements[left]:
                    elements[parent], elements[left] = elements[left], elements[parent]
            else:
                min_index = left
                if elements[right] < elements[left]:
                    min_index = right
                if elements[parent] > elements[min_index]:
                    elements[parent], elements[min_index] = elements[min_index], elements[parent]
            origin_parent -= 1
        while origin_parent >= 0:
            left = origin_parent * 2 + 1 + offset
            right = left + 1
            parent = origin_parent + offset
            min_index = left
            if elements[right] < elements[left]:
                min_index = right
            if elements[parent] > elements[min_index]:
                elements[parent], elements[min_index] = elements[min_index], elements[parent]
            origin_parent -= 1
    return elements


def merge_sort(elements):
    """
    Use the simple merge sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__ and __len__ were implemented,
    as well as the slice and add operations.
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    volume = 2
    while length > volume / 2:
        index = 0
        while length - index >= volume:
            tmp = []
            i, j, limit = index, index + volume / 2, index + volume
            mid_limit = j
            while i < mid_limit and j < limit:
                if elements[j] < elements[i]:
                    tmp.append(elements[j])
                    j += 1
                else:
                    tmp.append(elements[i])
                    i += 1
            if i < mid_limit:
                tmp += elements[i:mid_limit]
            else:
                tmp += elements[j:limit]
            for value in tmp:
                elements[index] = value
                index += 1
        if length - index > volume / 2:
            tmp = []
            i, j = index, index + volume / 2
            mid_limit = j
            while i < mid_limit and j < length:
                if elements[j] < elements[i]:
                    tmp.append(elements[j])
                    j += 1
                else:
                    tmp.append(elements[i])
                    i += 1
            if i < mid_limit:
                tmp += elements[i:mid_limit]
            else:
                tmp += elements[j:]
            for value in tmp:
                elements[index] = value
                index += 1
        volume *= 2
    return elements


def quick_sort(elements):
    """
    Use the simple non-recursive quick sort algorithm to sort the :param elements.
    :param elements: a sequence in which the function __get_item__, __len__ and insert were implemented
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    stack, limit = [], [0, length - 1]
    while stack or limit[1] - limit[0] > 0:
        while limit[1] - limit[0] > 0:
            i, j, tail = limit[0], limit[1] - 1, limit[1]
            if tail - i == 1:
                if elements[tail] > elements[i]:
                    i = tail
            else:
                while i < j:
                    while i < j and elements[i] <= elements[tail]:
                        i += 1
                    while j > i and elements[j] >= elements[tail]:
                        j -= 1
                    if i < j:
                        elements[i], elements[j] = elements[j], elements[i]
                        i += 1
                        j -= 1
            if i == j:
                if elements[i] < elements[tail]:
                    i += 1
                elif elements[i] > elements[tail]:
                    i = j
            elements[i], elements[tail] = elements[tail], elements[i]
            limit.append(i)
            stack.append(limit)
            limit = [limit[0], limit[2] - 1]
        if stack:
            top = stack.pop()
            limit = [top[2] + 1, top[1]]
    return elements
