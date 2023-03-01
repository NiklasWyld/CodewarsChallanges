def to_weird_case(words):
    i = 0
    n = ''
    
    for word in words:
        if word == ' ':
            i = -1
            n += word
        elif i % 2 == 0:
            n += word.upper()
        else:
            n += word.lower()
        i += 1
        
    return n
