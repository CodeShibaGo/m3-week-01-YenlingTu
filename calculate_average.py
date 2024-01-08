def find_average(numbers):
    if numbers==[]:
        return 0
    else :
        total=0
        for i in numbers:
            total=total+i
        return total/len(numbers)*1.0