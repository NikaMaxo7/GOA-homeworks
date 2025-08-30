def position(x,y,n):
    first_number = (y / x) - (x - 1) / 2
    
    the_answer = first_number + n
    
    return int(the_answer)