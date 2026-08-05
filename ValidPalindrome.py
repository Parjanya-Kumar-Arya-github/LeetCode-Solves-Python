def isPalindrome(self, s: str) -> bool:
    temp = ""
    for i in s:
        temp += i if i.isalnum() else ""

    temp = temp.lower()

    return temp[::-1]==temp