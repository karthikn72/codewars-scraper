def round_to_next5(n):
    if n%5!=0:
      return 5*((n//5)+1)
    else:
      return n