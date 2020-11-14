def last_digit(n1, n2):
  if n2==0: return 1
  elif int(str(n1)[-1])==0: return 0
  else:
    i=1
    digits=[]
    while int(str(int(str(n1)[-1])**i)[-1]) not in digits:
      digits.append(int(str(int(str(n1)[-1])**i)[-1]))
      i+=1
    return digits[(n2%len(digits))-1]