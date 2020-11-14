def in_array(array1, array2):
    finalset=[]
    for i in array1:
      for z in array2:
        if i in z: finalset.append(i)
    return sorted(list(set(finalset)))
          