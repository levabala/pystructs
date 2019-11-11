
from functools import reduce
from math import sqrt, log10
from typing import Tuple, List
from matplotlib.pyplot import plot, show, xlabel, ylabel, title, legend
from random import randrange, random

from numpy.random import random
import seaborn as sns
import pandas as pd
import numpy as np


def lineralRegression(values: List[Tuple[float, float]]) -> Tuple[float, float]:
  n = len(values)
  sumXY = reduce(lambda acc, t: acc + (lambda x, y: x * y)(*t), values, 0.0)
  sumX = reduce(lambda acc, t: acc + (lambda x, y: x)(*t), values, 0.0)
  sumY = reduce(lambda acc, t: acc + (lambda x, y: y)(*t), values, 0.0)
  sumX2 = reduce(lambda acc, t: acc + (lambda x, y: x ** 2)(*t), values, 0.0)

  a = (n * sumXY - sumX * sumY) / (n * sumX2 - sumX ** 2)
  b = (sumY - a * sumX) / n

  return (a, b)


def M(values: List[float]) -> float:
  return sum(values) / len(values)


def multiply(set1: List[float], set2: List[float]) -> List[float]:
  return list(map(lambda t: set1[t[0]] * t[1], enumerate(set2)))


def substract(set1: List[float], set2: List[float]) -> List[float]:
  return list(map(lambda t: set1[t[0]] - t[1], enumerate(set2)))


def decrease(s: List[float], value: float) -> List[float]:
  return list(map(lambda v: v - value, s))


def pow(s: List[float], power: float) -> List[float]:
  return list(map(lambda v: v ** power, s))


def covariance(set1: List[float], set2: List[float]) -> float:
  return M(multiply(set1, set2)) - M(set1) * M(set2)


def variance(s: List[float]) -> float:
  a = pow(s, 2)
  b = M(s) ** 2
  c = M(a)
  return c - b


def deviation(s: List[float]) -> float:
  return sqrt(variance(s))


def correlation(set1: List[float], set2: List[float]) -> float:
  return covariance(set1, set2) / (deviation(set1) * deviation(set2))


def getCompensationPoint(a: float, b: float, X: List[float], Y: List[float]):
  n = len(X)

  m = sum(Y)
  s = sum(X)
  l = sum(map(lambda x: x ** 2, X))
  k = sum(map(lambda t: (lambda i, x: x * Y[i])(*t), enumerate(X)))

  x0 = (a * s + b * l - k) / (a * n + b * s - m)
  y0 = a * (n + 1) - sum(Y) + b * (sum(X) + x0)

  print("{} {} ".format(x0, y0))

  return (x0, y0)


def gaussCached():
  global secondValue
  secondValue = 0.0

  def gauss():
    global secondValue

    if secondValue != 0.0:
      v = secondValue
      secondValue = 0.0
      return v

    while True:
      u = random() * 2 - 1
      v = random() * 2 - 1

      s = u ** 2 + v ** 2

      if s <= 1 and s != 0:
        r = sqrt(-2 * log10((s)) / s)

        secondValue = v * r
        return u * r

  return gauss


def getPoints(X: List[float], Y: List[float]):
  points: List[Tuple[float, float]] = sorted(
      list(map(lambda t: (X[t[0]], t[1]), enumerate(Y))))

  return points


def test3():
  data = pd.read_csv('files/prog2_input.csv')

  a = data["a"][0]
  b = data["b"][0]

  amount = 100
  maxX = 4000
  randomizationScale = 10

  X = [randrange(0, maxX) for _ in range(amount)]
  Y = [a * x + b for x in X]

  gauss = gaussCached()
  deviations = [gauss() * randomizationScale for _ in range(amount)]

  # gN = np.random.normal(Y, 1, 10)

  YDeviated = [Y[i] + deviations[i] for i in range(amount)]
  # print(gN)
  # print(YDeviated)

  points = getPoints(X, YDeviated)
  # pointsN = getPoints(X, gN)

  (a2, b2) = lineralRegression(points)

  plot(*zip(*points), 'go', label="generated points")
  # plot(*zip(*pointsN), 'yo', label="generated points")
  plot([0, maxX], [b, a * maxX + b], 'b', label="target regression")
  plot([0, maxX], [b2, a2 * maxX + b2], 'r', label="real regression")
  legend(loc='upper left')

  pd.DataFrame(points).to_csv("files/prog2_output.csv", index=False)

  show()


def test1():
  data = pd.read_csv('files/prog1_input.csv')
  views = data['views']
  downloads = data['downloads']

  points = sorted(
      list(map(lambda t: (views[t[0]], t[1]), enumerate(downloads))))
  (a, b) = lineralRegression(points)

  print("a: {}, b: {}".format(a, b))

  var = variance(views)
  dev = deviation(views)
  r = correlation(views, downloads)
  average = M(views)

  devN = np.std(views)
  varN = np.var(views)
  rN = np.corrcoef(views, downloads)

  print("devN: {}".format(devN))
  print("varN: {}".format(varN))
  print("rN: {}".format(rN))

  print("variance: {}".format(var))
  print("deviation: {}".format(dev))
  print("correlation: {}".format(r))
  print("average: {}".format(average))

  outputData = {
      "Variance": [var],
      "Deviation": [dev],
      "Correlation": [r],
      "Average": [average]
  }

  pd.DataFrame(outputData).to_csv("files/prog1_output.csv", index=False)

  xxx = list(map(lambda t: t[0], points))
  yyy = list(map(lambda t: t[1], points))

  regressionPointsX = [0, 10000]
  regressionPointsY = list(map(lambda x: x * a + b, regressionPointsX))

  plot(xxx, yyy, 'go', label="data poitns")
  plot(regressionPointsX, regressionPointsY, 'r', label="lineral regression")
  legend(loc='upper left')
  title('Task 1')
  xlabel('views')
  ylabel('downloads')

  # sns.lineplot(data=pd.DataFrame(
  #     {'x': regressionPointsX, 'y': regressionPointsY}))
  # sns.scatterplot(data=pd.DataFrame([xxx, yyy]))

  show()


if __name__ == '__main__':
  test1()
