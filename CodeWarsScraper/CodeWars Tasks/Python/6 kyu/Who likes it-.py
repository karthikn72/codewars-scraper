def likes(names):
    #your code here
    final=""
    if len(names)==0:
      final= "no one likes this"
    elif len(names)==1:
      final= names[0]+" likes this"
    elif len(names)==2:
      final=names[0]+" and "+names[1]+" like this"
    elif len(names)==3:
      final=names[0]+", "+names[1]+" and "+names[2]+" like this"
    else:
      final=names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this"
    return final