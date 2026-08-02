def isValid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for char in s:  
        if char in mapping.values():
            stack.append(char)  
        elif char in mapping.keys():
            if stack == [] or mapping[char] != stack.pop():
                return False    

    return stack == []
#This is a very famous problem in coding interviews. 
#The problem is basically to check for stack knowledge


#The best solution given:

def isValid(s):
    i=0
    a=[]
    for i in range(len(s)):
        if s[i]=='('or s[i]=='['or s[i]=='{':
            a.append(s[i])
        else:
            if not a:
                return False
            top=a.pop()
            if s[i]==')'and top!='(':
                return False
            if s[i]==']'and top!='[':
                return False
            if s[i]=='}'and top!='{':
                return False
    return len(a)==0


#Since Python is considered slower than others, it's runtime doesn't beat 100%
