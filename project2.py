import random
import time
import seaborn as sns
import matplotlib.pyplot as plt

def random_numbers_generator(size):
    return [random.randint(1, 10000) for _ in range(size)]

def random_numbers_generator3(size3):
    return [random.randint(1, 30000) for _ in range(size3)]

def random_numbers_generator5(size5):
    return [random.randint(1, 50000) for _ in range(size5)]

def random_numbers_generator7(size7):
    return [random.randint(1, 70000) for _ in range(size7)]

def random_numbers_generator9(size9):
    return [random.randint(1, 90000) for _ in range(size9)]



def bubble_Sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def shell_Sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def quicksort(arr):  
    if len(arr) < 2:  
        return arr  
    pivot = arr[0]  
    left = [x for x in arr[1:] if x < pivot]  
    right = [x for x in arr[1:] if x >= pivot]  
    return quicksort(left) + [pivot] + quicksort(right) 



sizes = [10000, 30000, 50000, 70000, 90000]

for size in sizes:
    random_numbers = random_numbers_generator(size)

    bubble_start_time = time.time() # start the clock
    bubble_Sort(random_numbers.copy()) # put your sorting method
    bubble_stop_time = time.time() - bubble_start_time # stop the clock and calculate the time difference

    shell_start_time = time.time() # start the clock
    shell_Sort(random_numbers.copy()) # put your sorting method
    shell_stop_time = time.time() - shell_start_time # stop the clock and calculate the time difference

    quicksort_start_time = time.time() # start the clock
    quicksort(random_numbers.copy()) #  put your sorting method
    quicksort_stop_time = time.time() - quicksort_start_time # stop the clock and calculate the time difference




for size3 in sizes:
    random_numbers = random_numbers_generator3(size3)

    bubble_start_time = time.time() # start the clock
    bubble_Sort(random_numbers.copy()) #  put your sorting method
    bubble_stop_time3 = time.time() - bubble_start_time # stop the clock and calculate the time difference

    shell_start_time = time.time() # start the clock
    shell_Sort(random_numbers.copy()) # put your sorting method
    shell_stop_time3 = time.time() - shell_start_time # stop the clock and calculate the time difference

    quicksort_start_time = time.time() # start the clock
    quicksort(random_numbers.copy()) #  put your sorting method
    quicksort_stop_time3 = time.time() - quicksort_start_time # stop the clock and calculate the time difference




for size5 in sizes:
    random_numbers = random_numbers_generator5(size5)

    bubble_start_time = time.time() # start the clock
    bubble_Sort(random_numbers.copy()) # put your sorting method
    bubble_stop_time5 = time.time() - bubble_start_time # stop the clock and calculate the time difference
    print("--- the sort tool %s seconds ---" % bubble_stop_time)

    shell_start_time = time.time() # start the clock
    shell_Sort(random_numbers.copy()) # put your sorting method
    shell_stop_time5 = time.time() - shell_start_time # stop the clock and calculate the time difference

    quicksort_start_time = time.time() # start the clock
    quicksort(random_numbers.copy()) #  put your sorting method
    quicksort_stop_time5 = time.time() - quicksort_start_time # stop the clock and calculate the time difference



for size7 in sizes:
    random_numbers = random_numbers_generator7(size7)

    bubble_start_time = time.time() # start the clock
    bubble_Sort(random_numbers.copy()) #  put your sorting method
    bubble_stop_time7 = time.time() - bubble_start_time # stop the clock and calculate the time difference

    shell_start_time = time.time() # start the clock
    shell_Sort(random_numbers.copy()) #  put your sorting method
    shell_stop_time7 = time.time() - shell_start_time # stop the clock and calculate the time difference

    quicksort_start_time = time.time() # start the clock
    quicksort(random_numbers.copy()) #  put your sorting method
    quicksort_stop_time7 = time.time() - quicksort_start_time # stop the clock and calculate the time difference



for size9 in sizes:
    random_numbers = random_numbers_generator9(size9)

    bubble_start_time9 = time.time() # start the clock
    bubble_Sort(random_numbers.copy()) # put your sorting method
    bubble_stop_time9 = time.time() - bubble_start_time # stop the clock and calculate the time difference

    shell_start_time = time.time() # start the clock
    shell_Sort(random_numbers.copy()) # put your sorting method
    shell_stop_time9 = time.time() - shell_start_time # stop the clock and calculate the time difference

    quicksort_start_time = time.time() # start the clock
    quicksort(random_numbers.copy()) # put your sorting method
    quicksort_stop_time9 = time.time() - quicksort_start_time # stop the clock and calculate the time difference

print("Bubble Sort")
print("10000   "  + bubble_stop_time)
print("30000   "  + bubble_stop_time3)
print("50000   "  + bubble_stop_time5)
print("70000   "  + bubble_stop_time7)
print("90000   "  + bubble_stop_time9)

print("\n")

print("Shell Sort")
print("10000   " + shell_stop_time)
print("30000   " + shell_stop_time3)
print("50000   " + shell_stop_time5)
print("70000   " + shell_stop_time7)
print("90000   " + shell_stop_time9)

print("\n")

print("Quicksort")
print("10000   "+ quicksort_stop_time)
print("30000   "+ quicksort_stop_time3)
print("50000   "+ quicksort_stop_time5)
print("70000   "+ quicksort_stop_time7)
print("90000   "+ quicksort_stop_time9)

x = [10000, 30000, 50000, 70000, 90000]
bubble_y = [bubble_stop_time, bubble_stop_time3, bubble_stop_time5, bubble_stop_time7, bubble_stop_time9]
sns.lineplot(x=x, y=bubble_y)
plt.xlabel('Number')
plt.ylabel('Time')
plt.title('Bubble Sort')


x = [10000, 30000, 50000, 70000, 90000]
shell_y = [shell_stop_time, shell_stop_time3, shell_stop_time5, shell_stop_time7, shell_stop_time9]
sns.lineplot(x=x, y=shell_y)
plt.xlabel('Number')
plt.ylabel('Time')
plt.title('Shell Sort')

x = [10000, 30000, 50000, 70000, 90000]
quicksort_y = [quicksort_stop_time, quicksort_stop_time3, quicksort_stop_time5, quicksort_stop_time7, quicksort_stop_time9]
sns.lineplot(x=x, y=quicksort_y)
plt.xlabel('Number')
plt.ylabel('Time')
plt.title('Quicksort')

