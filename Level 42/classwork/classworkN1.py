def unique_sum(lst):
    idk = []
    for i in lst:
        if i not in idk:
            idk.append(i)
    if not idk:
        return None
    return sum(idk)