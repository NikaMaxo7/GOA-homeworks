def full_string(lst):
    i = 0
    result = ""
    while i < len(lst):
        result += lst[i]
        i += 1
    return f"Results = {result}"

print(full_string(["N","i","k","a",]))