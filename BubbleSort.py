if __name__ == "__main__":
    li = [10, 5, 2, 8, 7]

    print(li)
    i = 0
    for i1 in range(len(li)):
        for j1 in range(len(li) - i - 1): # -1 because we'll check value of exact last with the last (8, 7)
            if li[j1] > li[j1 + 1]:
                li[j1], li[j1 + 1] = li[j1 + 1], li[j1]
                print(li)

    print(li)

    #     TIME COMPLEXITY : O(n^2)
