def dig_pow(n, p):
    # your code
    newnum=new=0
    for i in range(len(str(n))):
      newnum+=int(str(n)[i])**(p+i)
    z=check=1
    new=0
    while check!=0 and new!=newnum:
      new=n*z
      if new==newnum:
        check=0
        return z
      elif new>newnum:
        return -1
      z+=1
    return -1