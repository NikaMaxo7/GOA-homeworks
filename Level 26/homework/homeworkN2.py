def most_common_data_type(lst):
    if not lst:
        return None

    int_count = 0
    float_count = 0
    str_count = 0
    other_count = 0

    for item in lst:
        if type(item) == int:
            int_count += 1
        elif type(item) == float:
            float_count += 1
        elif type(item) == str:
            str_count += 1
        else:
            other_count += 1

    if int_count >= float_count and int_count >= str_count and int_count >= other_count:
        return 'int'
    elif float_count >= int_count and float_count >= str_count and float_count >= other_count:
        return 'float'
    elif str_count >= int_count and str_count >= float_count and str_count >= other_count:
        return 'str'
    else:
        return 'other'