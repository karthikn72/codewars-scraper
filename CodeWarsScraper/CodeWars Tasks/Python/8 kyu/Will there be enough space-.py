def enough(cap, on, wait):
    value=wait-(cap-on)
    if value>=0:
      return value
    return 0