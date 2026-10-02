def top_three_largest(values):
    if len(values) == 1 or len(values) == 0:
        return values
    # values: list of numbers
    # return the three largest values in descending order
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for value in values:

        if value > first:
            third = second
            second = first
            first = value

        elif value > second:
            third = second
            second = value

        elif value > third:
            third = value


    if(len(values) == 2):
        return [first , second]

    return [first , second, third]    
    
    pass