def categorize_new_member(data):
    new_arr=[]
    for i in data:
        if i[0]>=55 and i[1]>7:
            new_arr.append("Senior")
        else:
            new_arr.append("Open")
    return new_arr