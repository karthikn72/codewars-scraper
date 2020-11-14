def cakes(rec, av):
    try:
      items=[]
      reckeys=list(rec.keys())
      avkeys=list(av.keys())
      for i in range(len(reckeys)):
        items.append(av[reckeys[i]]//rec[reckeys[i]])
      return min(items)
    except KeyError:
      return 0