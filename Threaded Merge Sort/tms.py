import concurrent.futures


def merge_sort(l: list) -> list:
    """
    The merge sort algorithm.
    :param l: The unsorted list.
    :return: A sorted list.
    """
    # Stop condition, if length of list is just 1 we return it.
    if len(l) == 1:
        return l

    # Split the list
    l1 = l[:len(l) // 2]
    l2 = l[len(l) // 2:]

    # Merge sort the two split lists
    l1 = merge_sort(l1)
    l2 = merge_sort(l2)
    # Merge the two lists
    return merge(l1, l2)


def merge(l1: list, l2: list) -> list:
    """
    Function that supports merge sort by merging two lists.
    :param l1: List 1 to merge.
    :param l2: List 2 to merge
    :return: A sorted merged list.
    """
    s = []
    # While both lists still have data
    while l1 and l2:
        if l1[0] > l2[0]:
            s.append(l2[0])
            l2.pop(0)
        else:
            s.append(l1[0])
            l1.pop(0)

    # Only l1 has data left
    for i in l1:
        s.append(i)

    # Only l2 has data left.
    for i in l2:
        s.append(i)
    return s


def split_lists(data: list, thread_count: int) -> list:
    """
    A function that splits the list in multiple lists.
    :param data: List to split.
    :param thread_count: How many lists there need to be
    :return: A list with split lists.
    """
    # Split the list
    split_data = [data[:len(data) // 2], data[len(data) // 2:]]
    # Keep splitting the list till we have enough lists to distribute over all the threads.
    while len(split_data) < thread_count:
        tmp_split_data = []
        for i in split_data:
            tmp_split_data.append(i[:len(i) // 2])
            tmp_split_data.append(i[len(i) // 2:])
        split_data = tmp_split_data
    return split_data


def threaded_merge_sort(data: list, thread_count: int) -> list:
    """
    Takes care of all the setup needed for the multithreading part of merge sort.
    :param data: A unsorted list to sort.
    :param thread_count: How many threads need to be used.
    :return: A sorted list.
    """
    # If thread_count is only 0 or 1 we just use the main thread.
    if thread_count == 1 or thread_count == 0:
        return merge_sort(data)
    # For multithreading we use the pool executor.
    with concurrent.futures.ThreadPoolExecutor(max_workers=thread_count) as executor:
        # Split data to distribute it over the threads.
        split_data = split_lists(data, thread_count)
        threads = []
        results = []
        for index in range(thread_count):
            # Start the thread.
            r = executor.submit(merge_sort, split_data[index])
            # Add it to a list so we can keep track of it
            threads.append(r)
        # Loop over all the threads
        for t in threads:
            # Wait for the thread to finish and get its result.
            results.append(t.result())

    # After getting all the results from the threads we need to merge it all.
    i = 0
    while len(results) > 1:
        # We can easily use the merge function to merge all the results.
        results[i] = merge(results[i], results[i + 1])
        results.pop(i + 1)
        if i < len(results) - 2:
            i += 1
        else:
            i = 0
    # Return the sorted list.
    return results[0]

