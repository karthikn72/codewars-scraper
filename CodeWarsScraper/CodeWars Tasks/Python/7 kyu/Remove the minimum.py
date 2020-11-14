def remove_smallest(numbers):
    numbers2=[]
    for i in numbers:
       numbers2.append(i)
    if len(numbers2)>=1:
        a=min(numbers2)
        b=numbers2.count(a)
        if b>1:
          numbers2.pop(numbers2.index(a))
          return numbers2
        elif b==1:
          numbers2.pop(numbers2.index(a))
          return numbers2
    else:
       return numbers2
    raise NotImplementedError("TODO: remove_smallest")
