def spin_words(sentence):
    newsen=sentence.split(" ")
    new=""
    for i in range(len(newsen)):
      if len(newsen[i])>=5: new+=newsen[i][::-1]
      else: new+=newsen[i]
      if len(newsen)!=1 and i!=len(newsen)-1:
        new+=" "
    return new