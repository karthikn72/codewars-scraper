def productFib(prod):
    # your code
    fibs=[0,1]
    i=0
    anset=[]
    answer=0
    while answer<=prod:
      answer=fibs[i+1]+fibs[i]
      fibs.append(answer)
      i+=1
    for i in range(len(fibs)):
      if fibs[i]*fibs[i+1]==prod:
        anset.append(fibs[i])
        anset.append(fibs[i+1])
        anset.append(0==0)
        return anset
      elif fibs[i]*fibs[i+1]<prod and fibs[i+1]*fibs[i+2]>prod:
        anset.append(fibs[i+1])
        anset.append(fibs[i+2])
        anset.append(0==1)
        return anset

       