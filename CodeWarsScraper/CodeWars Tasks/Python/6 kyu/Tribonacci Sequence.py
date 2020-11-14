def tribonacci(signature, n):
    #your code here
    fibs=[]
    empty=[]
    for x in signature:
      fibs.append(x)
    i=0
    if n>=4:
      while len(fibs)!=n:
        fibs.append(fibs[i+2]+fibs[i+1]+fibs[i])
        i+=1
    elif n==2:
      return fibs[:2]
    elif n==1:
      return fibs[0:1]
    elif n==0:
      return empty
    return fibs
      