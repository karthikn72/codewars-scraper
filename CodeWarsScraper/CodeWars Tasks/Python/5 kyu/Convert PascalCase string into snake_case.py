def to_underscore(s):
    if str(s).isnumeric()==True: return str(s)
    string=""
    new=""
    for i in range(len(s)):
      if i==0:
        string+=s[i]
      if ord(s[i])<=90 and ord(s[i])>=65 and i!=0:
        new+=string.lower()+"_"
        string=s[i].lower()
      elif i!=0:
        string+=str(s[i])
    new+=string
    return new[:-1]+s[-1]