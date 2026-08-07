
#This was quite irritating, since it had very weird test cases, but still got it done.
#But this code can be made better

def myAtoi(s: str) -> int:
        
    upper_cap = 2**31-1
    lower_cap = -2**31
    ans=0
    neg=False
    num_found=False
    sign_found=False

    for i in range(len(s)):

        if (sign_found or num_found) and s[i]==" ":
            break

        elif s[i].isnumeric():
            num_found=True
            ans = ans*10 + int(s[i])

        elif (not num_found and (s[i]=='-' or s[i]=="+")):
            if sign_found:
                return 0
            sign_found=True
            neg = True if s[i]=="-" else False


        elif s[i]!=" ":
            break

        

    ans = -ans if neg else ans
    
    if (ans>upper_cap or ans<lower_cap ):
        return (upper_cap if ans>upper_cap else lower_cap)

    return ans


#Better and smaller code,
#The logic is same, but the code is smaller and more readable

def myAtoi(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-', '+']:
        s = s[1:]

    ans = 0
    for char in s:
        if not char.isdigit():
            break
        ans = ans * 10 + int(char)

    ans *= sign
    upper_cap = 2**31 - 1
    lower_cap = -2**31

    if ans > upper_cap:
        return upper_cap
    elif ans < lower_cap:
        return lower_cap

    return ans