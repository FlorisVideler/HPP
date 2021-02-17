def bucket_sort_function(data: list, k: int = None, p: int = 0) -> list:
    """
    This function sorts a list using bucket sort. Used by the bucket_sort function.
    :param data: The list of ints to sort.
    :param k: The length of the largest number in the list.
    :param p: Times the function has run.
    :return: A sorted list.
    """
    # The stop condition, if the times we run the sort is equal to the max size of the ints we stop.
    if p * -1 == k:
        return data
    # Init the bucket list
    bucket_list = [[], [], [], [], [], [], [], [], [], []]
    for i in data[:]:
        # We try to get the right int to check what bucket is needed. Is this fails for some reason
        # (example: "-" is found instead of an int) we do leave the data where it is.
        try:
            check = int(str(i)[p - 1])
            bucket_list[check].append(i)
            data.remove(i)
        except:
            pass

    # Add data from buckets back to the original data.
    for i in bucket_list:
        data += i

    # Recursively repeat this.
    return bucket_sort_function(data, k, p - 1)


def bucket_sort(data: list) -> list:
    """
    Splits a list in negative and positive numbers and bucket sorts them individually.
    :param data: List of unsorted ints.
    :return: Sorted list
    """
    pos = []
    neg = []
    # Separate the positive numbers from the negative numbers.
    for i in data:
        if i < 0:
            neg.append(i)
        else:
            pos.append(i)
    # Before returning the combination of the 2 lists we reverse the negative list.
    # We also subtract 1 from lenght of the longeste int because of the "-" symbol.
    return list(reversed(bucket_sort_function(neg, len(str(min(neg))) - 1))) + bucket_sort_function(pos,
                                                                                                    len(str(max(pos))))
