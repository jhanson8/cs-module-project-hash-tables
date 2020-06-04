from collections import Counter 


def no_dups(s):
    # Your code here
    words = s.split()
    cache = {}
    no_dupes = []
    space = " "
    if s == "":
        return ""
    for word in words:
        if word not in cache:
            cache[word] = word
            no_dupes.append(word)
    return space.join(no_dupes) 
        

 




if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))