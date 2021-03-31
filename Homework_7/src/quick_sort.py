def quicksort(x):
    
    def recursive(start, end):
        if start >= end:
            return

        l, r = start, end - 1
        pivot = x[end]

        while l <= r:
            while l <= r:
                if x[l] > pivot:
                    break
                l += 1
            while l <= r:
                if x[r] < pivot:
                    break
                r -= 1
            
            if l <= r:
                x[l], x[r] = x[r], x[l]
                
        x[l], x[end] = x[end], x[l]
        recursive(start, l - 1)
        recursive(l + 1, end)

    recursive(0, len(x) - 1)
    print(x)


if __name__ == '__main__':
    # x = [5, 3, 7, 6, 2, 1, 4]
    # quicksort(x)
    x = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quicksort(x)