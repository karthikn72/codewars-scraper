def isValidWalk(walk):
    vertical=0
    horizontal=0
    for i in walk:
      print(i,horizontal,vertical)
      if i=="n": vertical+=1
      if i =="s": vertical-=1
      if i=="e": horizontal+=1
      if i=="w": horizontal-=1
    if vertical==0 and horizontal==0:
      return len(walk)==10
    return False