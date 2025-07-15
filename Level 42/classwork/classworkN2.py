def doubles(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    
    result = ""
    for i in stack:
        result = result + i
    
    return result