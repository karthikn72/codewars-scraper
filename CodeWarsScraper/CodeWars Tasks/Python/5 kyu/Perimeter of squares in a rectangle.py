def perimeter(n):
    # your code
    fibs=[0,1]
    for i in range(n):
      fibs.append(fibs[i+1]+fibs[i])
    return 4*(sum(fibs))