def number(bus_stops):
    people = 0
    for i in bus_stops:
        people += i[0]
        people -= i[1]
    return people