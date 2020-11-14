def nb_dig(n, d):
    count=0
    numset=[i**2 for i in range(n+1) if str(d) in str(i**2)]
    for i in numset:
      count+=str(i).count(str(d))
    return count



    