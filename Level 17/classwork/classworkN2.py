# შექმენით manual_append ფუნქცია

def manual_append(L, x):
    res = []
    for i in L:
        res += [i]
    res += [x]
    
    return res

print(manual_append([1,2,3,4,5],6))