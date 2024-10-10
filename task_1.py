import random
import timeit

# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Генерація тестових наборів
def generate_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Використання timeit для вимірювання часу
def measure_time(sort_function, data):
    timer = timeit.Timer(lambda: sort_function(data.copy()))
    return timer.timeit(number=1)

# Тестові дані
sizes = [100, 1000, 5000]
test_cases = {
    "Random Data": [generate_data(size) for size in sizes],
    "Sorted Data": [sorted(generate_data(size)) for size in sizes],
    "Reversed Data": [sorted(generate_data(size), reverse=True) for size in sizes]
}

# Порівняння алгоритмів
for case_name, data_sets in test_cases.items():
    print(f"--- {case_name} ---")
    for size, data in zip(sizes, data_sets):
        print(f"Data Size: {size}")
        print(f"Merge Sort: {measure_time(merge_sort, data):.6f} seconds")
        print(f"Insertion Sort: {measure_time(insertion_sort, data):.6f} seconds")
        print(f"Timsort (Python's sorted): {measure_time(sorted, data):.6f} seconds")
