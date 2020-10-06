if __name__ == "__main__":
    li = [11, 3, 2, 6, 5, 8, 7, 4, 9, 0, 14, 10, 1, 8]
    min = 0
    index = 0
    print(li)
    while index < len(li):
        for i in range(index, len(li)):
            if i == index or li[i] < li[min]:
                min = i

        if li[index] > li[min]:
            li[index], li[min] = li[min], li[index]

        index += 1
        print(li)


#     TIME COMPLEXITY : n+n-1+n-2+......+1
#                         n * (n -1) / 2
#                           1/2 (n^2 - n)
#                             O(n^2)
