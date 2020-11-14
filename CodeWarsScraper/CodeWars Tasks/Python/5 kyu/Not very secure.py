def alphanumeric(string):
    count=0
    for i in string:
      if (ord(i)<=122 and ord(i)>=97) or (ord(i)<=57 and ord(i)>=48) or (ord(i)<=90 and ord(i)>=65):
        count+=1
    return count==len(string)