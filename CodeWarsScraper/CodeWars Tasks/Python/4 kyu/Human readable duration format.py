def format_duration(seconds):
    if seconds == 0:
      return "now"
    else:
      origin = seconds
      dic = {'year':31536000,'day':86400,'hour':3600,'minute':60,'second': 1}
      spent = {}
      ans = ""
      for x in ['year','day','hour','minute','second']:
          spent[x] = seconds // dic[x]
          ans += "{}{} {}{}".format('' if seconds==origin else ' and ' if seconds % dic[x] == 0 else ', ',spent[x],x,'s' if spent[x] > 1 else '') if spent[x] > 0 else ''
          seconds %= dic[x]
      return  ans