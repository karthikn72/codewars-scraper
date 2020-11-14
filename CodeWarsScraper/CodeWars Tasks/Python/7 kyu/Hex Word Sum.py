def hex_word_sum(string):
    # C0DE
    string=string[::-1]
    words=string.split()
    sum2=0
    sum1=0
    start=1
    check=0
    for word in words:
      start=1
      sum1=0
      if check==0:
          sum2+=sum1
      check=0
      for i in word:
        if i=="A":
          sum1+=10*start
          start=start*16
        elif i=="B":
          sum1+=11*start
          start=start*16
        elif i=="C":
          sum1+=12*start
          start=start*16
        elif i=="D":
          sum1+=13*start
          start=start*16
        elif i=="E":
          sum1+=14*start
          start=start*16
        elif i=="F":
          sum1+=15*start
          start=start*16
        elif i=='S':
          sum1+=5*start
          start=start*16
        elif i=='O':
          start=start*16
        else:
            sum1=0
            break
      sum2+=sum1
      check=1
    return sum2
