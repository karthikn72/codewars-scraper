def fib(n):
    #your code here
    fibs=[0,1]
    for i in range(n):
      fibs.append(fibs[i+1]+fibs[i])
    return fibs[n-1]