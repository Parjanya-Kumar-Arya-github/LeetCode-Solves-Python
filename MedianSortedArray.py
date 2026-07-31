#My Solution: 
# (since time compplexity asked is O(log(m+n)), 
# I have used binary search to find the median of two sorted arrays)

def medianOf2(a, b):
    n = len(a)
    m = len(b)

    # if a[] has more elements, then call medianOf2 
    # with reversed parameters
    if n > m:
        return medianOf2(b, a)

    lo = 0
    hi = n
    while lo <= hi:
        mid1 = (lo + hi) // 2
        mid2 = (n + m + 1) // 2 - mid1
    
        # find elements to the left and right 
        # of partition in a[]
        l1 = (mid1 == 0) and float('-inf') or a[mid1 - 1]
        r1 = (mid1 == n) and float('inf') or a[mid1]

        # find elements to the left and right 
        # of partition in b[]
        l2 = (mid2 == 0) and float('-inf') or b[mid2 - 1]
        r2 = (mid2 == m) and float('inf') or b[mid2]

        # if it is a valid partition
        if l1 <= r2 and l2 <= r1:
          
            # if the total elements are even, then median is 
            # the average of two middle elements
            if (n + m) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
              
            # if the total elements are odd, then median is 
            # the middle element
            else:
                return max(l1, l2)

        # check if we need to take lesser 
        # elements from a[]
        if l1 > r2:
            hi = mid1 - 1
            
        # check if we need to take more 
        # elements from a[]
        else:
            lo = mid1 + 1
    return 0

if __name__ == "__main__":
    a = [-5, 3, 6, 12, 15]
    b = [-12, -10, -6, -3, 4, 10]
    print(medianOf2(a, b))