def choose_best_sum(t, k, ls):
    import itertools
    possible=list(set(itertools.combinations(range(len(ls)),k)))
    checkset=[]
    for i in possible:
      check=0
      for index in range(len(i)):
        check+=ls[i[index]]
      checkset.append(check)
    checkset=sorted(checkset, reverse=True)
    for i in checkset:
      if i<=t:
        return i


    