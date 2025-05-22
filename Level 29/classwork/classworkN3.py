def is_vow(inp):
    result = []
    
    for number in inp:
        letter = chr(number)
        
        if letter in 'aeiou':
            result.append(letter)
        else:
            result.append(number)
            
    return result