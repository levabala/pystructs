from dataclasses import dataclass
from point import Point
from typing import Tuple, Any, Callable
from toolz import pipe, curry, compose
from math import atan2, sqrt
from functools import singledispatch
from multipledispatch import dispatch

# pylint: disable=function-redefined


@dataclass
class Vector:
  dx: float
  dy: float

  def __str__(self):
    return "{}, {}".format(self.dx, self.dy)


def argAsTuple(f: Callable):
  return lambda t: f(*t)


def vector(p1: Point, p2: Point) -> Vector:
  return p2 - p1
