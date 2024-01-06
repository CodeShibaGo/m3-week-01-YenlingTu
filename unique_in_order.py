def unique_in_order(iterable):
    new = []
    for i in iterable:
        if len(new)==0 or i!=new[-1]:
            new.append(i)
    return new