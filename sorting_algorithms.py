"""
Implementation of 7 Sorting Algorithms

Created on 25th April 2020
Developed by Shubhankar-wdsn

This is a OOP based implementation of some of the most common sorting algorithms I am aware of.
To understand the principle behind inheritence and polymorphism, I have used OOP instead of
functional programming. However, using functions would be an easier and a much more efficient option.

"""

import random, time

class Algorithm:
    def __init__(self, name):
        self.array = random.sample(range(900), 900)
        self.name = name

    def update_display(self, swap1=None, swap2=None):
        import sorting_visualiser

        sorting_visualiser.update(self, swap1, swap2)

    def run(self):
        self.start_time = time.time()
        self.algorithm()
        time_elapsed = time.time() - self.start_time
        return self.array, time_elapsed


class SelectionSort(Algorithm):
    def __init__(self):
        super().__init__("SelectionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            self.update_display(self.array[i], self.array[min_idx])


class BubbleSort(Algorithm):
    def __init__(self):
        super().__init__("BubbleSort")

    def algorithm(self):
        for i in range(len(self.array)):
            for j in range(len(self.array)-1-i):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
            self.update_display(self.array[j], self.array[j+1])


class InsertionSort(Algorithm):
    def __init__(self):
        super().__init__("InsertionSort")

    def algorithm(self):
        for i in range(len(self.array)):
            cursor = self.array[i]
            idx = i
            while idx > 0 and self.array[idx-1] > cursor:
                self.array[idx] = self.array[idx-1]
                idx -= 1
            self.array[idx] = cursor
            self.update_display(self.array[idx], self.array[i])

class RadixSort(Algorithm):
    def __init__(self):
        super().__init__("RadixSort")

    def algorithm(self):

        def counting_sort(self, exp):
            output = [0] * len(self.array)
            count = [0] * (10)
            for i in range(0, len(self.array)):
                idx = (self.array[i]//exp)
                count[int((idx)%10)] += 1
            for i in range(1,10):
                count[i] += count[i-1]
            i = len(self.array)-1
            while i >= 0:
                idx = (self.array[i]/exp)
                output[count[int((idx)%10)]-1] = self.array[i]
                count[int((idx)%10)] -= 1
                i -= 1
            i = 0
            for i in range(len(self.array)):
                self.array[i] = output[i]
                self.update_display(self.array[i])

        maximum = max(self.array)
        exp = 1
        while maximum // exp > 0:
            counting_sort(self, exp)
            exp *= 10

class MergeSort(Algorithm):
    def __init__(self):
        super().__init__("MergeSort")

    def algorithm(self, array=[]):
        if array == []:
            array = self.array
        if len(array) < 2:
            return array
        mid = len(array) // 2
        left = self.algorithm(array[:mid])
        right = self.algorithm(array[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
            self.update_display()
        result += left[i:]
        result += right[j:]
        self.array = result
        self.update_display()
        return result

class QuickSort(Algorithm):
    def __init__(self):
        super().__init__("QuickSort")

    def algorithm(self, array=[], start=0, end=0):
        if array == []:
            array = self.array
            end = len(array) - 1
        if start < end:
            pivot = self.partition(array,start,end)
            self.algorithm(array,start,pivot-1)
            self.algorithm(array,pivot+1,end)

    def partition(self, array, start, end):
        x = array[end]
        i = start-1
        for j in range(start, end+1, 1):
            if array[j] <= x:
                i += 1
                if i < j:
                    array[i], array[j] = array[j], array[i]
                    self.update_display(array[i], array[j])
        return i

class HeapSort(Algorithm):
    def __init__(self):
        super().__init__("HeapSort")

    def heapify(self, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.array[i] < self.array[left]:
            largest = left
        if right < n and self.array[largest] < self.array[right]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.update_display(self.array[i], self.array[largest])
            self.heapify(n, largest)

    def algorithm(self):
        n = len(self.array)
        for i in range(n,-1,-1):
            self.heapify(n, i)
        for i in range(n-1,0,-1):
            self.array[i], self.array[0] = self.array[0], self.array[i]
            self.heapify(i, 0)



