def rgb(r, g, b):
    #your code here :)
    def check(z):
      test=str(hex(z))[2:]
      if len(test)==1:
        return "0"+test
      elif z<=0:
        return "00"
      elif z>=256:
        return "FF"
      else:
        return str(test).upper()
    return check(r)+check(g)+check(b)