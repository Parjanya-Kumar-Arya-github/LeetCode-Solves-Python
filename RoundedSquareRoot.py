#Brute Force

def mySqrt(self, x: int) -> int:
    t=1
    while(t*t<=x):
        t+=1

    return t-1

#Best Binary Method

def mySqrt(self, x):
    if x < 2:
        return x
    
    left, right = 1, x // 2
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return right