def iq_test(numbers):
    #your code here
    numset1=[]
    numset=[]
    numbers=str(numbers)
    numbers=numbers.split()
    for i in numbers:
        i=int(i)
        numset1.append(i)
        numset.append(i%2)
    if numset.count(0)>numset.count(1):
      return (numset.index(1)+1)
    else:
      return (numset.index(0)+1)