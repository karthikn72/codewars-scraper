def move_zeros(array):
    #your code here
    x=array.count(0)
    newarr=[]
    for i in array:
      if str(i)=="False":
        newarr.append(0==1)
        x-=1
      if i!=0:
        newarr.append(i)
    for y in range(x):
      newarr.append(0)
    return newarr
      