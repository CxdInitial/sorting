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


def bucket_sort(elements, bucket_size=10):
    """
    Use the simple bucket sort algorithm to sort the :param elements.
    :param bucket_size: the distribution buckets' size
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
    buckets_size = (maxi - mini + 1) // bucket_size
    if (maxi - mini + 1) % bucket_size:
        buckets_size += 1
    buckets = []
    for i in range(buckets_size):
        buckets.append([None, None])
    for element in elements:
        index = element // bucket_size
        ptr = buckets[index]
        while ptr[1] and ptr[1][0] < element:
            ptr = ptr[1]
        element = [element, ptr[1]]
        ptr[1] = element
    length = 0
    for bucket in buckets:
        ptr = bucket[1]
        while ptr:
            elements[length] = ptr[0]
            length += 1
            ptr = ptr[1]
    return elements
