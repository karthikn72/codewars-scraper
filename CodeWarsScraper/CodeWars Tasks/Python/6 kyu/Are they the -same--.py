def comp(array1, array2):
    try:
      array1=sorted(array1)
      array2=sorted(array2)
      count=0
      for i in range(len(array1)):
        if array1[i]**2==array2[i]:
          count+=1
      return count==len(array1)
    except:
      if type(array1)=='NoneType' and type(array2)=='NoneType': return True
      return False
    