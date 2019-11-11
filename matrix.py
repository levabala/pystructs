from functools import reduce
from typing import List, Tuple
from math import floor

# (unit, amount)
Element = float

Matrix = List[List[Element]]

Edge = Tuple[Element, Element]

Vector = List[Element]


def matrixFromStr(values: List[str]) -> Matrix:
  m = list(map(lambda l: list(map(lambda el: float(el), l.split(' '))), values))
  return m


def transpose(m: Matrix) -> Matrix:
  return reduce(lambda acc, val: list(map(lambda t: (lambda i, column: [*column, val[i]])(*t), acc)), m, list(map(lambda el: [], m[0])))


def shell(width: int, height: int) -> Matrix:
  m = [[0.0] * width for i in range(height)]
  return m


def edges(m: Matrix, oriented=False) -> List[Edge]:
  rows = enumerate(m)
  selector = lambda columnIndex, element: element != 0
  rowProcessor = lambda rowIndex, row: map(lambda elem: (
      min(rowIndex, elem[0]), max(rowIndex, elem[0])
  ), filter(lambda t: selector(*t), enumerate(row)))
  edges = reduce(lambda acc, row: [*acc, *rowProcessor(*row)], rows, [])

  return list(set(edges))


def findComponents(m: Matrix) -> List[int]:
  comp = [0] * len(m)
  num = 0

  for v in range(len(m)):
    if comp[v] == 0:
      num = dfs(m, v, num + 1, comp)

  return comp


def dfs(m: Matrix, v: int, num: int, comp: List[int]) -> int:
  comp[v] = num
  adjacent: List[int] = list(
      map(lambda t: t[0], filter(lambda t: t[1] == 1, enumerate(m[v]))))

  for u in adjacent:
    if comp[u] == 0:
      return dfs(m, u, num, comp)

  return num


# def parseEdges(edgesStr: List[str]) -> Matrix:
#   edges = list(map(lambda es: (lambda v1, v2: (int(v1), int(v2)))
#                    (*es.split(' ')), edgesStr))
#   maxV = reduce(lambda acc, edge: max(max(edge[0], edge[1]), acc), edges, 0)

#   def applyEdge(mm: Matrix, ee: (int, int)) -> Matrix:
#     v1 = ee[0]
#     v2 = ee[1]
#     row = mm[v1]
#     mm[v1][v2] = 1.0
#     mm[v2][v1] = 1.0

#     return mm

#   m = reduce(lambda acc, edge:  shell(maxV, maxV)


# if __name__ == '__main__':
#   m = [
#       [0, 1, 0, 0, 0, 0],
#       [1, 0, 1, 1, 0, 0],
#       [0, 1, 0, 1, 0, 0],
#       [0, 1, 1, 0, 0, 0],
#       [0, 0, 0, 0, 0, 1],
#       [0, 0, 0, 0, 1, 0],
#   ]

#   comp = findComponents(m)
#   print(comp)
