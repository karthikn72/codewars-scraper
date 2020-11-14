# Should return triangle type:
#  0 : if triangle cannot be made with given sides
#  1 : acute triangle
#  2 : right triangle
#  3 : obtuse triangle

def triangle_type(a, b, c):
  sides=sorted([a,b,c])
  a=sides[0]
  b=sides[1]
  c=sides[2]
  if a+b<=c: return 0
  elif (a**2)+(b**2)==(c**2): return 2
  elif (a**2)+(b**2)<(c**2): return 3
  return 1
  