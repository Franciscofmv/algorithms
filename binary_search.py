

def binary_search(target: int,l: list[int]):
    """
    Expects an ordered list l.
    """
    low = 0
    high = len(l) - 1
    while  low <= high:
        mid = (low + high) // 2
        guess = l[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid -1
        else:
            low = mid + 1
        
        return 0
            


def main():
    l1 = [1,2,3,4,5,6,7,8,9]
    t1 = 4
    print(binary_search(t1, l1))


if __name__ == "__main__":
    main()