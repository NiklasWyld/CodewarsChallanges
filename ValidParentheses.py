def valid_parentheses(string):
    x = []
    
    for l in string:
        if(l == '('):
            x.append(l)
        elif(l == ')'):
            try:
                x.pop()
            except:
                return False

    if(len(x) == 0):
        return True
    else:
        return False
