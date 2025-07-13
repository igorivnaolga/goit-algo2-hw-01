# Реалізуйте функцію, яка знаходить максимальний та мінімальний
# елементи в масиві, використовуючи метод «розділяй і володарюй».


def find_min_max(arr):
    # Base case: one element
    if len(arr) == 1:
        return arr[0], arr[0]

    # Base case: two elements
    if len(arr) == 2:
        return (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])

    # Divide array in two halves
    mid = len(arr) // 2
    left_min, left_max = find_min_max(arr[:mid])
    right_min, right_max = find_min_max(arr[mid:])

    # Combine results
    return min(left_min, right_min), max(left_max, right_max)


arr = [3, 25, 1, 18, -6, 7, 44]
min_val, max_val = find_min_max(arr)
print(f"Min: {min_val}, Max: {max_val}")
