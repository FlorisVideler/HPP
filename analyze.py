from bucket_sort import bucket_sort
import time, random
from tabulate import tabulate
from statistics import pstdev


def bucket_sort_general(q: int = 1000, n: int = 1000) -> tuple:
    """
    Tests the bucket sort with a bunch of random numbers.
    :param q: How many times is the test going to run.
    :param n: How long will the input list be.
    :return: A list with a times and whether all the lists came back sorted.
    """
    times = []
    correct = True
    for i in range(q):
        random_list = [random.randint(-100000, 100000) for iter in range(n)]
        start_time = time.time()
        bucket_sort_result = bucket_sort(random_list)
        times.append(time.time() - start_time)
        if bucket_sort_result != sorted(random_list):
            correct = False
    return correct, times


def bucket_sort_sorted_list(q: int = 1000, n: int = 1000):
    """
    Tests the bucket sort algorithm with a sorted list.
    :param q: How many times is the test going to run.
    :param n: How long will the input list be.
    :return: A list with times of how long it took to sort.
    """
    times = []
    for i in range(q):
        sorted_list = sorted([random.randint(-100000, 100000) for iter in range(n)])
        start_time = time.time()
        bucket_sort(sorted_list)
        times.append(time.time() - start_time)
    return times


def bucket_sort_reversed_list(q: int = 1000, n: int = 1000):
    """
    Tests the bucket sort function with a reversed sorted list.
    :param q: How many times is the test going to run.
    :param n: How long will the input list be.
    :return: A list with times of how long it took to sort.
    """
    times = []
    for i in range(q):
        sorted_list = list(reversed(sorted([random.randint(-100000, 100000) for iter in range(n)])))
        start_time = time.time()
        bucket_sort(sorted_list)
        times.append(time.time() - start_time)
    return times


def bucket_sort_unique_list(q: int = 1000, n: int = 1000):
    """
    Tests the bucket sort function with a list filled with unique random numbers.
    :param q: How many times is the test going to run.
    :param n: How long will the input list be.
    :return: A list with times of how long it took to sort.
    """
    times = []
    for i in range(q):
        sorted_list = random.sample(range(-100000, 100000), n)
        start_time = time.time()
        bucket_sort(sorted_list)
        times.append(time.time() - start_time)
    return times


def analyze_all(q: int = 100, n: int = 75000):
    """
    Function that calls all the other functions that analyze the algorithm. Also formats the results in a nice table
    :param q: How many times is the test going to run.
    :param n: How long will the input list be.
    :return: A table with the results.
    """
    total_start_time = time.time()
    sort_correct, sort_results = bucket_sort_general(q, n)
    print('sort_correct')
    sort_sorted_list = bucket_sort_sorted_list(q, n)
    print('sort_sorted_list')
    sort_reversed_list = bucket_sort_reversed_list(q, n)
    print('sort_reversed_list')
    sort_unique_list = bucket_sort_unique_list(q, n)

    headers = ['Type', 'Avg', 'Min', 'Max', 'Std']
    table = [['Bucket sort normal', sum(sort_results) / len(sort_results), min(sort_results), max(sort_results),
              pstdev(sort_results)],
             ['Bucket sort sorted list', sum(sort_sorted_list) / len(sort_sorted_list), min(sort_sorted_list),
              max(sort_sorted_list), pstdev(sort_sorted_list)],
             ['bucket sort reversed list', sum(sort_reversed_list) / len(sort_reversed_list), min(sort_reversed_list),
              max(sort_reversed_list), pstdev(sort_reversed_list)],
             ['bucket sort unique values', sum(sort_unique_list) / len(sort_unique_list), min(sort_unique_list),
              max(sort_unique_list), pstdev(sort_unique_list)]]

    print(f'Running all the metrics took {time.time() - total_start_time} seconds')
    print(f'Bucket sort correct = {sort_correct}')
    print(f'Each metric is calculated with a population of {q} and a list length of {n}')
    print(tabulate(table, headers=headers))
    return table


# Run the main function.
if __name__ == '__main__':
    analyze_all()
