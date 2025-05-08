def remove_different_type(lst):
    only_ints = []
    for item in lst:
        if type(item) == int:
            only_ints.append(item)

    if len(lst) - len(only_ints) == 1:
        return only_ints
    else:
        return lst