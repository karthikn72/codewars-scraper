def sequence_sum(begin_number, end_number, step):
    #your code here
    new=begin_number
    newsum=new
    while new<=end_number:
      new+=step
      newsum+=new
    if begin_number<=end_number:
      return newsum-new
    return 0