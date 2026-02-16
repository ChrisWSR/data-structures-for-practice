import time
import random
import sys
import math
maxRecursion = 100000
sys.setrecursionlimit(maxRecursion)

ordenar = [random.randint(1, 9999) for i in range(100)]
## insetion sort
#ordenar = [847, 312, 659, 128, 934, 571, 245, 783, 419, 156, 
#             892, 637, 284, 501, 768, 923, 345, 612, 879, 146,
#             523, 790, 357, 614, 881, 238, 695, 452, 819, 176,
#             543, 900, 267, 724, 481, 838, 195, 652, 409, 866,
#             223, 780, 537, 94, 651, 318, 875, 432, 789, 256,
#             713, 470, 827, 384, 941, 598, 165, 722, 489, 846,
#             313, 770, 527, 984, 451, 108, 665, 422, 879, 236,
#             593, 950, 317, 774, 541, 98, 655, 422, 789, 356,
#             813, 570, 237, 794, 461, 118, 675, 432, 899, 256,
#             713, 580, 347, 904, 571, 238, 795, 462, 129, 786]
#
def execution_time(func):
    def wrapper(*args,**kwargs):
        start =  time.time()
        result = func(*args,**kwargs)
        end = time.time()
        total_time = end - start
        print(f"Execution time of funtion {func.__name__}: {total_time:.6f} seconds")
        #return result
    return wrapper
@execution_time
def insertion_sort(array):
    for i in range(1,len(array)):
        j = i
        while array [j -1] > array[j] and j > 0:
            array[j-1],array[j] = array[j],array[j-1]
            j-=1
    
    return array




## Selection sort
@execution_time
def selection_sort(array):
    for i in range(len(array)):
        smallest =i
        for j in range(i+1,len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i],array[smallest] = array[smallest],array[i]
    

    return array


## bubble sort

@execution_time
def bubble_sort(array):
    for i in range(len(array)-1):
        has_swapped = False
        for j in range(len(array)-1,i,-1):
            if array[j-1] > array[j]:
                array[j -1],array[j] = array[j],array[j -1]
                has_swapped = True
        if not has_swapped:
            break
    

    return array

@execution_time
def shell_sort(array):
    gaps = [5,3,1]
    for gap in gaps:
        for i in range(gap,len(array)):
            j = i - gap
            while array[j+gap] < array[j] and j>=0:
                array[j], array[j+gap] = array[j+gap],array[j]
                j-= gap
    

    return array

@execution_time
def heap_sort(array):
    heapify(array)
    for end_idx in range(len(array) - 1, 0 ,-1):
        array[0],array[end_idx] = array[end_idx],array[0]
        move_down(array,0,end_idx -1)
    

    return array

def heapify(array):
    last_nonleaf_idx = len(array)//2-1
    for i in range(last_nonleaf_idx, -1,-1):
        move_down(array,i,len(array)-1)
    

    return array

def move_down(array,start_idx,end_idx):
    child_idx =2 *start_idx + 1
    while child_idx <= end_idx:
        if child_idx < end_idx and array[child_idx] < array[child_idx + 1]:
            child_idx += 1
        if array[start_idx] < array[child_idx]:
            array[start_idx], array[child_idx] = array[child_idx],array[start_idx]
            start_idx = child_idx
            child_idx = 2*start_idx + 1
        else:
            child_idx = end_idx + 1
@execution_time
def merge_sort(array):
    def _merge_sort_r(arr):
        if len(arr) < 2:
            return arr
        first_half = _merge_sort_r(arr[:len(arr)//2])
        second_half = _merge_sort_r(arr[len(arr)//2:])
        return merge(first_half,second_half)
    return _merge_sort_r(array)

def merge(first_half, second_half):
    result = []
    i = j = 0
    while i< len(first_half) and j < len(second_half):
        if first_half[i] < second_half[j]:
            result.append(first_half[i])
            i +=1
        else:
            result.append(second_half[j])
            j+=1
    while i< len(first_half):
        result.append(first_half[i])
        i+=1
    while j<len(second_half):
        result.append(second_half[j])
        j+=1
    return result

def partition(array,start,end):
    if start >=end:
        return array
    pivot = end
    boundary = start
    for i in range(start,end):
        if array[i] <= array[pivot]:
            array[boundary], array[i] = array[i],array[boundary]
            boundary+=1
    array[boundary],array[end] = array[end],array[boundary]
    partition(array,start,boundary -1)
    partition(array,boundary+1,end)
    return array

@execution_time
def quick_sort(array):
    if len(array)<2:
        return array
    return partition(array,0,len(array)-1)
    
@execution_time
def radix_sort(array):
    max_digits = get_max_number_of_digits(array)
    for i in range(max_digits + 1): 
        buckets = [[] for _ in range(10)]
        for num in array:
            digit = get_digit_at_position(num,position=i)
            buckets[digit].append(num)
        array = flatten(buckets)
    return array
def get_max_number_of_digits(array):
    return max(int(math.log10(abs(num))) + 1 if num != 0 else 1 for num in array)

def get_digit_at_position(number,position):
    return (abs(number) // 10 ** position)%10

def flatten(array):
    return [num for inner in array for num in inner]


seleccion_array = ordenar.copy()
insert_array = ordenar.copy()
bubble_array = ordenar.copy()
shell_array = ordenar.copy()
heap_array = ordenar.copy()
merge_array = ordenar.copy()
quick_array = ordenar.copy()
radix_array = ordenar.copy()


print("\n")
#print("selection sort", selection_sort(seleccion_array))
#print("Insertion sort", insertion_sort(insert_array))            
#print("bubble sort", bubble_sort(bubble_array))            
#print("shell sort", shell_sort(shell_array))            
print("heap sort", heap_sort(heap_array))
print("merge sort", merge_sort(merge_array))
print("quick sort", quick_sort(quick_array))
print("radix sort", radix_sort(quick_array))
