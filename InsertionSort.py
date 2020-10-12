'''
Time complexity : For best case O(n) and Worst case O(n^2)
Space Complexity : O(n) // n == size of li
'''

if __name__ == "__main__":
    li = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2]

    for i in range(1, len(li)):
        k = i
        while k != 0:
            if li[k] < li[k - 1]:
                li[k], li[k - 1] = li[k - 1], li[k]  # swap
                print(li)
            k -= 1
    print(li)
