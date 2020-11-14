def whatday(num):
  # Put your code here
  days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
  if num<=7 and num>=1:
    return days[num-1]
  else:
    return ("Wrong, please enter a number between 1 and 7")

  