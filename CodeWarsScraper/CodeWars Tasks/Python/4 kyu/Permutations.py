def permutations(string):
    #your code here
    import itertools
    string3=itertools.permutations(string)
    string3=set(string3)
    string3=list(string3)
    string4=(''.join(w) for w in string3)
    return string4

    