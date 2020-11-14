def duplicate_count(text):
    text=text.lower()
    check=list(set([i for i in text]))
    num=0
    for i in check:
      x=text.count(i)
      if x!=1: num+=1
    return num
     