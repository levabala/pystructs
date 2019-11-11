from math import sqrt
from typing import List, Callable, Tuple
from functools import reduce


def matExp(values: List[Tuple[float, float]]) -> float:
  """Matematical expectation"""
  reducer: Callable[[float, Tuple[float, float]]
                    ] = lambda acc, val: acc + val[0] * val[1]
  return reduce(reducer, values, 0)


def variance(values: List[Tuple[float, float]]) -> float:
  """Variance"""
  values2 = pow(values, 2)
  return matExp(values2) - matExp(values) ** 2


def deviation(values: List[Tuple[float, float]]) -> float:
  """Standart deviation"""
  return sqrt(variance(values))


def pow(values: List[Tuple[float, float]], power: float) -> List[Tuple[float, float]]:
  return list(map(lambda t: (t[0] ** power, t[1]), values))

# def poissonDistribution(n, p, m) -> float


if __name__ == "__main__":
  X = [(-3, 0.05), (-1, 0.1), (2, 0.4), (3.5, 0.2), (5, 0.15), (9, 0.1)]

  v = variance(X)
  d = deviation(X)

  print(v)
  print(d)
