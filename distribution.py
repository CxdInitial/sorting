def counting_sort(elements):
    """
    Use the simple counting sort algorithm to sort the :param elements.
    :param elements: a integer sequence in which the function __get_item__ and __len__ were implemented()
    :return: the sorted elements in increasing order
    """
    length = len(elements)
    if not length or length == 1:
        return elements
    mini = maxi = elements[0]
    for element in elements:
        assert isinstance(element, int)
        if element < mini:
            mini = element
        if element > maxi:
            maxi = element
    all_range = []
    for i in range(maxi - mini + 1):
        all_range.append(0)
    for element in elements:
        all_range[element - mini] += 1
    length = 0
    for i in range(len(all_range)):
        count = all_range[i]
        while count > 0:
            elements[length] = i + mini
            length += 1
            count -= 1
    return elements
