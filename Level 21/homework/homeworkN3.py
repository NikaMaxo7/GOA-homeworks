def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) in (int, float):
        return "Who ate the last cookie? It was Monica!"
    elif type(x) == bool:
        return "Who ate the last cookie? It was the dog!"