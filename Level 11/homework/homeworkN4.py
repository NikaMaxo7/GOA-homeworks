def count_char_occurrences(s, char):
    count = 0
    
    for i in s:
        if i == char:
            count += 1
    
    return count
