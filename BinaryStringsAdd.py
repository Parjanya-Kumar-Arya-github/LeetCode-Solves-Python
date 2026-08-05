def addBinary(self, a: str, b: str) -> str:
    BinRes = ""
    carry = "0"

    if len(a)>len(b):
        b= "0"*(len(a)-len(b))+b
    else:
        a = "0"*(len(b)-len(a))+a
    
    print(a,b)

    for i in range(len(a)-1,-1,-1):
        if a[i]==b[i]:
            BinRes = carry + BinRes
            carry = "1" if a[i]=="1" else "0"
        elif (a[i]=="0" and b[i]=="1") or (a[i]=="1" and b[i]=="0"):
            BinRes = ("0" if carry == "1" else "1") + BinRes
            carry = "1" if carry == "1" else "0"

    return (str(int(carry+BinRes)))