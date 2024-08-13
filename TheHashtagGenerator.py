def generate_hashtag(s):
    if not s:
        return False
    
    is_word = False
    
    new_s = '#'
    
    for letter in s:
        if letter == ' ':
            is_word = False
        else:
            if is_word:
                new_s = new_s + letter.lower()
            else:
                new_s = new_s + letter.upper()
            is_word = True

    
    if len(new_s) > 140:
        return False
    
    return new_s
