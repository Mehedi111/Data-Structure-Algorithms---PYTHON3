def merge(a, b):
    output = []  # output list
    a_index, b_index = 0, 0  # initial index for both a & b
    while a_index < len(a) and b_index < len(b):  # if any of index reach the length than break loop
        # print(f"check sort{a_index, b_index, a[a_index], b[b_index]}")
        if a[a_index] < b[b_index]:
            output.append(a[a_index])
            a_index += 1
        else:
            output.append(b[b_index])
            b_index += 1
        # print(f"{output}")

    if a_index == len(a):
        # if a index equal to length that means b index not reach to last, because loop will break when it'll be false
        # at first condition
        # and b_index has element what is not included in output
        output.extend(b[b_index:])  # so add remain of b to the out put
    else:  # otherwise b index equal to length than a's length is larger than b
        # and a_index has element what is not included in output
        output.extend(a[a_index:])
    return output


def merge_sort(a):
    if len(a) <= 1:  # a list with 0 or one element is sorted
        return a
    print(a)

    #  split the list in half and call merge sort recursively on each half
    left = merge_sort(a[:len(a) // 2])
    print(f"after left {a}")
    right = merge_sort(a[len(a) // 2:])

    return merge(left, right)


if __name__ == '__main__':
    l = [1, 5, 6, 3, 9, 8, 4, 7, 2]
    print(merge_sort(l))
