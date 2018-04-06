

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


def _quick_sort(arr, low, high):
    if low >= high:
        return

    mid = partition(arr, low, high)

    _quick_sort(arr, low, mid-1)
    _quick_sort(arr, mid+1, high)


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr)-1)

