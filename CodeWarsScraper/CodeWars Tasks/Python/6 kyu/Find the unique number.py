def find_uniq(arr):
    # your code here
    import statistics
    a=statistics.mode(arr)
    for i in arr:
      if i!=a:
        return i  # n: unique integer in the array