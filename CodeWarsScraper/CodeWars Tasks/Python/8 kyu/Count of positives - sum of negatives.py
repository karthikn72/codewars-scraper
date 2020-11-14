def count_positives_sum_negatives(arr):
    new=count=0
    for i in arr:
      if i>0:
        count+=1
      elif i<0:
        new+=i
    if len(arr)>0:
      return [count,new]
    return []