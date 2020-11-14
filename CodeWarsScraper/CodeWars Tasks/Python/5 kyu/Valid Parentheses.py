def valid_parentheses(string):
    a=-1
    b=-1
    while string.count("(")==string.count(")") and string.count("(")!=0:
      a=string.find("(",a+1)
      b=string.find(")",b+1)
      if a>b and a!=-1:
        return False
      elif a==-1:
        return True
    if string.count("(")==string.count(")") and string.count("(")==0:
      return True
    return False


      