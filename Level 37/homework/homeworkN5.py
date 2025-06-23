def find_next_square(sq):
    root = int(sq ** 0.5)
    
    if root * root != sq:
        return -1
    
    next_root = root + 1
    
    return next_root * next_root