def get_grade(s1, s2, s3):
    points = s1 + s2 + s3
    answer = points / 3
    if answer <= 100 and answer >= 90:
        return "A"
    elif answer < 90 and answer >=80:
        return "B"
    elif answer < 80 and answer >=70:
        return "C"
    elif answer < 70 and answer >=60:
        return "D"
    else:
        return "F"