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
