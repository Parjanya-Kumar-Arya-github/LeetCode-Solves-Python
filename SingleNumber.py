#My Method is basically a brute force method.


def singleNumber(nums):
    final_list = []

    for i in nums:
        if i in final_list:
            final_list.remove(i)
        else:
            final_list.append(i)
    return final_list[0]     

#Best Method is to implement XOR operation.

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result