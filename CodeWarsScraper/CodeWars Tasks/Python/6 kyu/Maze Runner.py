def maze_runner(maze, directions):
    # Code Here
    for i in maze:
      for z in range(len(i)):
        if i[z]==2:
          x=maze.index(i)
          y=z
    check=check2=check3=0
    for i in maze:
      for z in range(len(i)):
        if i[z]==2:
          x=maze.index(i)
          y=z
    check=check2=check3=0
    x1=x
    y1=y
    for i in directions:
                  if i=="N":
                    x-=1
                  elif i=="E":
                    y+=1
                  elif i=="W":
                    y-=1
                  elif i=="S":
                    x+=1
                  if x>len(maze)-1 or y>len(maze)-1 or x<0 or y<0 or maze[x][y]==1:
                    return ("Dead")
                  elif maze[x][y]==3:
                    return ("Finish")
    return ("Lost")