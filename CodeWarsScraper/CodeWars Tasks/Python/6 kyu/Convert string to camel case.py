import re

def to_camel_case(text):
    text2=re.split("[-_]",text)
    new=""
    for i in range(len(text2)):
      if i==0 and len(text2)==1 and text2[i]=="": return new
      elif i==0 and text2[i][0].isupper(): new+=text2[i].title()
      elif i==0: new+=text2[i]
      else: new+=text2[i].title()
    return new