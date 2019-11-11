#!/usr/bin/env python


import contextlib as __stickytape_contextlib

@__stickytape_contextlib.contextmanager
def __stickytape_temporary_dir():
    import tempfile
    import shutil
    dir_path = tempfile.mkdtemp()
    try:
        yield dir_path
    finally:
        shutil.rmtree(dir_path)

with __stickytape_temporary_dir() as __stickytape_working_dir:
    def __stickytape_write_module(path, contents):
        import os, os.path

        def make_package(path):
            parts = path.split("/")
            partial_path = __stickytape_working_dir
            for part in parts:
                partial_path = os.path.join(partial_path, part)
                if not os.path.exists(partial_path):
                    os.mkdir(partial_path)
                    open(os.path.join(partial_path, "__init__.py"), "w").write("\n")

        make_package(os.path.dirname(path))

        full_path = os.path.join(__stickytape_working_dir, path)
        with open(full_path, "w") as module_file:
            module_file.write(contents)

    import sys as __stickytape_sys
    __stickytape_sys.path.insert(0, __stickytape_working_dir)

    __stickytape_write_module('matrix.py', "from functools import reduce\nfrom typing import List, Tuple\nfrom math import floor\n\n# (unit, amount)\nElement = float\n\nMatrix = List[List[Element]]\n\nEdge = Tuple[Element, Element]\n\nVector = List[Element]\n\n\ndef matrixFromStr(values: List[str]) -> Matrix:\n  m = list(map(lambda l: list(map(lambda el: float(el), l.split(' '))), values))\n  return m\n\n\ndef transpose(m: Matrix) -> Matrix:\n  return reduce(lambda acc, val: list(map(lambda t: (lambda i, column: [*column, val[i]])(*t), acc)), m, list(map(lambda el: [], m[0])))\n\n\ndef edges(m: Matrix, oriented=False) -> List[Edge]:\n  rows = enumerate(m)\n  selector = lambda columnIndex, element: element != 0\n  rowProcessor = lambda rowIndex, row: map(lambda elem: (\n      min(rowIndex, elem[0]), max(rowIndex, elem[0])\n  ), filter(lambda t: selector(*t), enumerate(row)))\n  edges = reduce(lambda acc, row: [*acc, *rowProcessor(*row)], rows, [])\n\n  return list(set(edges))\n")
    from matrix import edges, matrixFromStr
    
    size: int = int(input())
    lines = [input().strip() for i in range(size)]
    
    # lines = [
    #     [0, 0, 1, 0, 0],
    #     [0, 0, 1, 0, 1],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0],
    #     [0, 1, 0, 0, 0]
    # ]
    
    m = matrixFromStr(lines)
    e = edges(m)
    
    incremented = list(map(lambda t: (lambda a, b: (a + 1, b + 1))(*t), e))
    s = "\n".join(
        map(lambda t: (lambda a, b: "{} {}".format(a, b))(*t), incremented))
    
    print(s)
    