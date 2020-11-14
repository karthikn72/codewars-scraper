def row_sum_odd_numbers(n):
    start=[(n**2)-(n-1)]
    for i in range(n-1):
      start.append(start[-1]+2)
    return sum(start)
    