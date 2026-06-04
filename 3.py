import math

THRESHOLD = 3

def merge(arr, left, mid, right, depth):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:left + n1]
    right_arr = arr[mid + 1:mid + 1 + n2]

    indent = "  " * depth
    print(indent + "Сливаем {} и {}".format(left_arr, right_arr))

    i = j = 0
    k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, left, right, depth):
    if left >= right:
        return

    length = right - left + 1

    if length <= THRESHOLD:
        indent = "  " * depth
        print(indent + "Размер {} (≤ порога), вставками: {}".format(length, arr[left:right+1]))
        print(indent + "Результат вставок: {}".format(arr[left:right+1]))
        return

    mid = left + (right - left) // 2
    indent = "  " * depth
    print(indent + "Делим: {}".format(arr[left:right+1]))
    print(indent + "  Левая: [{}..{}]".format(left, mid))
    print(indent + "  Правая: [{}..{}]".format(mid+1, right))

    merge_sort(arr, left, mid, depth + 1)
    merge_sort(arr, mid + 1, right, depth + 1)

    merge(arr, left, mid, right, depth)

    print(indent + "После слияния: {}".format(arr[left:right+1]))

def main():
    arr = [38, 27, 43, 3, 9, 82, 10]

    print("Исходный массив:", arr)
    print("Порог:", THRESHOLD)
    print("РАЗДЕЛЕНИЕ И СЛИЯНИЕ")

    merge_sort(arr, 0, len(arr) - 1, 0)

    print("РЕЗУЛЬТАТ")
    print("Отсортированный массив:", arr)

    levels = int(math.log(len(arr)) / math.log(2)) + 1
    print("Уровней рекурсии (примерно):", levels)
    print("Использовано дополнительной памяти: O(n) на каждом уровне")

if __name__ == "__main__":
    main()
