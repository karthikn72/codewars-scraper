def validBraces(string):
  check=0
  string2=string
  p1=string2[0:(len(string)//2)]
  p2=string2[(len(string2)//2):len(string2)]
  if len(string2)%2==0 and len(string2)!=2:
      p2=p2[::-1]
      p2=p2.replace(")","(")
      p2=p2.replace("]","[")
      p2=p2.replace("}","{")
      if p1==p2:
        return True
      else:
        for i in range(len(string)):
            checkstr=""
            if string[i]=="(":
              a=string.find(")", i+1)
              a2=string.count(")")
              a3=string.count("(")
              if a!=-1 and a2==a3:
                checkstr=string[i:a]
                if len(checkstr)==2:
                  return True
                elif len(checkstr)%2==0:
                  if string[i:((a+1-i)//2)-1]==string[((a+1-i)//2):a]:
                    check=1
                  else:
                    return False
              else:
                return False
            elif string[i]=="{":
              b=string.find("}", i+1)
              b2=string.count("}")
              b3=string.count("}")
              if b!=-1 and b2==b3:
                checkstr=string[i:b]
                if len(checkstr)==2:
                  return True
                elif len(checkstr)%2==0:
                  if string[i:((b+1-i)//2)-1]==string[((b+1-i)//2):b]:
                    check=1
                  else:
                    return False
              else:
                return False
            elif string[i]=="[":
              c=string.find("]", i+1)
              c2=string.count("]")
              c3=string.count("[")
              if c!=-1 and c2==c3:
                checkstr=string[i:c]
                if len(checkstr)==2:
                  return True
                elif len(checkstr)%2==0:
                  if string[i:((c+1-i)//2)-1]==string[((c+1-i)//2):c]:
                    check=1
                  else:
                    return False
              else:
                return False
  else:
    for i in range(len(string)):
      checkstr=""
      if string[i]=="(":
        a=string.find(")", i+1)
        a2=string.count(")")
        a3=string.count("(")
        if a!=-1 and a2==a3:
          checkstr=string[i:a]
          if len(checkstr)==2:
            return True
          elif len(checkstr)%2==0:
            if string[i:((a+1-i)//2)-1]==string[((a+1-i)//2):a]:
              check=1
            else:
              return False
        else:
          return False
      elif string[i]=="{":
        b=string.find("}", i+1)
        b2=string.count("}")
        b3=string.count("}")
        if b!=-1 and b2==b3:
          checkstr=string[i:b]
          if len(checkstr)==2:
            return True
          elif len(checkstr)%2==0:
            if string[i:((b+1-i)//2)-1]==string[((b+1-i)//2):b]:
              check=1
            else:
              return False
        else:
          return False
      elif string[i]=="[":
        c=string.find("]", i+1)
        c2=string.count("]")
        c3=string.count("[")
        if c!=-1 and c2==c3:
          checkstr=string[i:c]
          if len(checkstr)==2:
            return True
          elif len(checkstr)%2==0:
            if string[i:((c+1-i)//2)-1]==string[((c+1-i)//2):c]:
              check=1
            else:
              return False
        else:
          return False
  return True        