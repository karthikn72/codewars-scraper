def power_of_two(x):
  # your code here
  powers=bin(x)
  if str(powers).count("1")==1:
    return True
  return False