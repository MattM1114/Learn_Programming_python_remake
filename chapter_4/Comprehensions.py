#squares = [0, 1, 4, 9, ..., n**2]
#squares = list()
#for x in range(n+1):
#    squares.append(x**2)

#squares = [x**2 for x in range(n+1)]
squares = set()
for x in range(n+1):
    squares.add(x**2)

squares = {x**2 for x in range(n+1)}