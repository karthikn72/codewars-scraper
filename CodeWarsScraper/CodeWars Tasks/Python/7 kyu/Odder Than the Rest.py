def odd_one(arr):
    for i in range(len(arr)):
      if arr[i]%2==1: return i
    return -1