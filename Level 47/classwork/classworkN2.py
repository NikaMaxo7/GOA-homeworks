def generate_pairs(n):
    result = []
    for a in range(n + 1):
        for b in range(a, n + 1):
            result.append([a, b])
    return result