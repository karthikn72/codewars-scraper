def longest(s1, s2):
    # your code
    new=[]
    for i in range(len(s1)):
      if s1[i] not in new:
        new.append(s1[i])
    print(new)
    for i in range(len(s2)):
      if s2[i] not in new:
        new.append(s2[i])
    if len(new)!=0:
      new.sort()
      return ''.join(new)
    else:
      return ''.join(new)