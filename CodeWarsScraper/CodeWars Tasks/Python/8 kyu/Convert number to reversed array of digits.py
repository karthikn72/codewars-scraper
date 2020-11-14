def digitize(n):
    n=str(n)
    n=n[::-1]
    nset=[]
    for i in n:
      nset.append(int(i))
    return (nset)