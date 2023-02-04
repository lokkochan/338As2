import json
import sys
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)
def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


# Open the file
with open('Q2.json', 'r') as f:
    # Read the file
    data = json.load(f)


performance = []
for i in range(len(data)):
    start = timeit.default_timer()
    func1(data[i], 0, len(data[i])-1)
    stop = timeit.default_timer()
    performance.append(stop - start)

plt.plot(performance)
plt.ylabel('Time')
plt.xlabel('Input Size')
plt.show()