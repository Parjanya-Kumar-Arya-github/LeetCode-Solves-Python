def reverse(x: int) -> int:
    ans = (int(str(x)[::-1]) if x>0 else -int(str(-x)[::-1]))
    if ans > 2 ** 31 - 1 or ans < -2 ** 31:
        return 0
    return ans