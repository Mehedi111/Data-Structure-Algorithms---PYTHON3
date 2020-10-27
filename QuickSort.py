# Divide and Conquer

def quick_sort(items, low, high):
    if low >= high:
        return items

    pivot = partition(items, low, high)

    print(f"piv {pivot}, low{low}, high {high}")

    quick_sort(items, low, pivot - 1)
    quick_sort(items, pivot + 1, high)
    return items


def partition(items, low, pivot):
    print(f"in partition {items[low:pivot], low, pivot}")
    i = low - 1
    piv = items[pivot]
    for j in range(low, pivot):
        # we consider the value which is less than pivot
        # if we got value less than pivot than this value will be swap with previous value, and we
        # increment the i for track that the position of changed/sort index
        if piv > items[j]:
            i += 1
            items[i], items[j] = items[j], items[i]
            print(items[low:pivot], i)

    # i is the position where all the values before i is less than pivot
    # after the loop done, we know that i+1 position is the suit position for pivot, so swap pivot position
    if items[i + 1] > items[pivot]:
        items[i + 1], items[pivot] = items[pivot], items[i + 1]
        print(f"values after 1st: {items[low:pivot]}")

    # items is sort now
    return i + 1


if __name__ == '__main__':
    # s = [6, 3, 8, 4, 7, 5]
    s = [10, 2, 14, 4, 7, 6]
    print(quick_sort(s, 0, len(s) - 1))
