def even_numbers(arr,n):
    arr.reverse()
    i=counter=0
    anset=[]
    while counter!=n:
      if arr[i]%2==0:
        anset.append(arr[i])
        counter+=1
      i+=1
    anset.reverse()
    return anset

      