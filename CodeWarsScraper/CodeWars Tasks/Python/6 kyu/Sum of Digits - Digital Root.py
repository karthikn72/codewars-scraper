def digital_root(n):
    # ...
    n=str(n)
    check=0
    sum=n
    while check!=1:
      sum2=0
      for i in str(sum):
        sum2+=int(i)
      sum=sum2
      if len(str(sum2))==1:
        check=1
        return sum