if __name__ == "__main__":
    li = [10, 5, 2, 8, 7]

    for i in range(len(li)):
        print("div1", li[i])

    for i in range(len(li) - 1):
        print("div2", li[i])

    print(li)
    i = 0
    for i1 in range(len(li)):
        for j1 in range(len(li) - i - 1): # -1 because we'll check value of exact last with the last (8, 7)
            if li[j1] > li[j1 + 1]:
                li[j1], li[j1 + 1] = li[j1 + 1], li[j1]
                print(li)

    print(li)

    #     TIME COMPLEXITY : O(n^2)
