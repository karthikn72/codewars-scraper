def anagrams(word, words):
    import itertools
    check=sorted(list(set(itertools.permutations(word))))
    new1=[]
    new=[]
    for i in check:
      new1.append(''.join(i))
    for z in words:
      if z in new1:
        new.append(z)
    return (new)