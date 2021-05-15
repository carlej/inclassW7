import string

def palan(word):
    l = len(word)
    half = int(l/2)
    a = 0
    while True:
        if a == half:
            return True
        if word[a] != word[l-a-1]:
            return False
        a+=1
