class Point:
  def __init__(self, x:int, y:int, rd:str):
    self.x = x
    self.y = y
    self.rd = rd

class XPointLine(Point):
  def __init__(self, xi:int, xf:int, y:int, rd:str):
    super().__init__(x=None, y=y, rd=rd)
    self.xi = xi
    self.xf = xf
  
class YPointLine(Point):
  def __init__(self, yi:int, yf:int, x:int, rd:str):
    super().__init__(x=x, y=None, rd=rd)
    self.yi = yi
    self.yf = yf

def graph(gx:int, gy:int, vectors:list, all:str):
  final_graph = {}

  i = gy
  while i > 0:
    final_graph[i] = ('x ' * gx).split()
    i -= 1

  for row in final_graph.values():
    i = 0
    while i < len(row):
      row[i] = row[i].replace('x', all)
      i += 1

  for vec in vectors: 
    if type(vec) == Point:
      final_graph[vec.y][vec.x-1] = vec.rd
    elif type(vec) == XPointLine:
      i = vec.xf
      while i >= vec.xi:
        final_graph[vec.y][i-1] = vec.rd
        i -= 1
    elif type(vec) == YPointLine:
      i = vec.yf
      while i >= vec.yi:
        final_graph[i][vec.x-1] = vec.rd
        i -= 1

  return final_graph