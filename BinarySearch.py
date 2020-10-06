if __name__ == "__main__":
    def search(li, match):
        if li[0] > match:
            return
        print(li)
        ln = len(li)
        mid = (ln - 1) // 2 if ln % 2 == 1 else ln // 2
        if li[mid] > match:
            li = li[0: mid]
            search(li, match)
        elif li[mid] < match:
            li = li[mid: ln]
            search(li, match)
        else:
            print(f"matched at {mid}")

    li = [1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71]
    search(li, 1)

    # Ieration solution will be easy rather than recursion.
    # Time complexity = O(log2^n)
    # Space Complexity = O(1)