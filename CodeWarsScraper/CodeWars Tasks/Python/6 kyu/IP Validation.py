def is_valid_IP(string):
    checkset=str(string).split(".")
    for i in checkset:
      a=i.isnumeric()
      b=i.find(" ")
      c=i.find("0")
      if a==True and len(checkset)==4 and b==-1:
        if int(i)>255 or int(i)<0:
          return False
        elif len(i)>1 and c==0:
          return False
      else:
        return False
    return True

    