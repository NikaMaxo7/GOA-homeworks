from preloaded import FIRST_NAME, SURNAME

def alias_gen(f_name: str, l_name: str) -> str:
    if not ('A' <= f_name[0].upper() <= 'Z') or not ('A' <= l_name[0].upper() <= 'Z'):
        return "Your name must start with a letter from A - Z."
    
    first = f_name[0].upper()
    last = l_name[0].upper()
     
    return FIRST_NAME[first] + " " + SURNAME[last]