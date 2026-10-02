def top_three_largest(values):
    if len(values) == 1 or len(values) == 0:
        return values
    # values: list of numbers
    # return the three largest values in descending order
    first = float('-inf')
    second = float('-inf')
    third = float('-inf')

    for i in values:
        first = max(first , i)

    freq_first = 1
    
    for i in values:
        if(i == first and freq_first == 1):
            freq_first = freq_first-1
            continue
        
        second = max(second , i)

    freq_sec = 2 if first == second else 1
    freq_first = 1

    for i in values:
        if(first == second and freq_first != 0):
            freq_first = freq_first-1
            continue
        
        if(i == first and freq_first == 1):
            freq_first = freq_first-1
            continue
        
        if(i == second and freq_sec == 1):
            freq_sec = freq_sec-1
            continue
        
        third = max(third , i)

    if len(values) == 2:
        return [first , second]

    return [first , second, third]    
    
    pass