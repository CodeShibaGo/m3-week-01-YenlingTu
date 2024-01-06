def find_capitals(capitals): 
    new_str=""
    for i in capitals:
        if i==i.upper() and i!=" ":
            new_str+=i
    return new_str
