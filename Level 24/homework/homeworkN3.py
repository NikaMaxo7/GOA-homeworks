def abbrev_name(name):
    name_parts = name.split(" ")
    
    first_initial = name_parts[0]
    second_initial = name_parts[1]
    
    first_name = first_initial[0].upper()
    last_name = second_initial[0].upper()
    
    return first_name + "." + last_name