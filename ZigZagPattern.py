def convert(self, s: str, numRows: int) -> str:
        changedS = ""

        if numRows == 1:
            return s

        inc = (numRows - 1) * 2

        for i in range(numRows):
            k = inc - i*2
            for j in range(i,len(s),inc):
                changedS+=s[j]
                if (k!=inc and not (j+k >= len(s)) and k!=0):
                    changedS+=s[j+k]
                

        return(changedS)