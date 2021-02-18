from threaded_merge_sort import threaded_merge_sort
import random
import matplotlib.pyplot as plt
import time


def plot(x: list, y: list, n: int, name: str = str(int(time.time()))) -> str:
    """
    Plot the data given.
    :param x: The data for the x axis.
    :param y: The data for the y axis.
    :param n: The length of the list that was sorted.
    :param name: The name used to save the file (excluding the file extension).
    :return: The name of the file.
    """
    # Initialize all the settings for the plot.
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(xlabel='threads', ylabel='time in seconds',
           title=f'Groei in thread count vs de tijd (n = {n})')
    plt.grid()
    # Save the plot.
    plt.savefig(f'{name}.png')
    # Show the plot.
    plt.show()
    return f'{name}.png'


def analyze_threaded_merge_sort(n: int = 30000, tpt: int = 50, t: int = 8) -> str:
    """
    Analyzes the threaded performance of merge sort.
    :param n: The length of the list to sort.
    :param tpt: Amount of times to test every thread.
    :param t: Amount of threads to use, calculated by 2^t.
    :return: Name of the file of the plot.
    """
    x = []
    y = []
    # We loop over all the threads
    for tc in range(t):
        # Save the results.
        results = []
        # Calculate the thread count.
        thread_count = 2 ** tc
        # We run every thread tpt times.
        for _ in range(tpt):
            random_list = [random.randint(-9999999, 9999999) for iter in range(n)]
            start_time = time.time()
            threaded_merge_sort(random_list, thread_count)
            results.append(time.time() - start_time)
        # Print the count to keep track of how long it takes.
        print(tc)
        # We take the average of all the times.
        y.append(sum(results) / len(results))
        x.append(thread_count)
    # Plot the results.
    return plot(x, y, n)


# Execute the script.
if __name__ == "__main__":
    tts = time.time()
    analyze_threaded_merge_sort(n=100000, tpt=25, t=15)
    print(f'took {time.time() - tts}')
