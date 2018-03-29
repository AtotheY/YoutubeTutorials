def backspace(inputString):
    myStack = []
    for char in inputString:
        if char != '<':
            myStack.append(char)
        else:
            myStack.pop()
    return ''.join(myStack)


inp = "aa<bb<cc<dd<e<<"

print backspace(inp)
