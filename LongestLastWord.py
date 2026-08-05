def LengthOfLastWord(s: str) -> int:
    longest_len = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] == " " and longest_len != 0 :
            return longest_len

        elif s[i] != " ": 
            longest_len+=1
    return longest_len