def distinct(seq):
    new_arr=[]
    for i in seq:
        if i in new_arr:
            print(i)
        else:
            new_arr.append(i)
    return new_arr