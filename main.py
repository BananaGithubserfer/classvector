from vector import Vector

first = Vector(1, 1, 22, 22)
print('-first', -first)

second = Vector(-1, -1, -22, -22)

third = first + second
print('first + second', third)

first += second
print('first += second', first)

print('second - zero vector', second - first)
