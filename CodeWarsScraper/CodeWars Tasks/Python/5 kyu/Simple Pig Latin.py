def pig_it(text):
    text=text.split(" ")
    newtext=""
    for i in text:
      if i.isalnum()==True: newtext+=i[1:]+i[0]+"ay "
      else: newtext+=i
    return newtext.strip(" ")