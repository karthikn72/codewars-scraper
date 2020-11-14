def find_outlier(integers):
    nums=[]
    for i in integers:
      nums.append(i%2)
    a=nums.count(0)
    a1=nums.index(0)
    b=nums.count(1)
    b1=nums.index(1)
    if a==1:
      return integers[a1]
    elif b==1:
      return integers[b1]

    return None