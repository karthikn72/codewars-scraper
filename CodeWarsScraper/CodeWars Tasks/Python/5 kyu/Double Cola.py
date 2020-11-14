def whoIsNext(names, r):
    # your code
    i= 5
    r-=1
    while r>=i:
      r-=i
      i*= 2
    return names[r//(i//5)]