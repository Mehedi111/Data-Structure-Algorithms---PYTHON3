
if __name__ == "__main__":
    li = [1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71]
    search = 55

    for item in range(len(li)):
        if li[item] == search:
            print(f"Found {search}")
            break

    # Time complexity = O(n)
    # Space Complexity = O(1)