# Write Python 3 code in this online editor and run it.
def duplicate_count(text):
    text=text.lower()
    new=[]
    for i in text:
        if text.count(i)>1 and i not in new:
            new.append(i)
            
    return len(new)