import random

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
BUILDING = [0]
BUILDING_TUPLE = []

i = 0
o = 1
while i <= 1000:
    if o % 2 == 0:
        u = random.randint(BUILDING[o - 2], BUILDING[o - 2] + 110)
        BUILDING.append(u)
        o += 1
        i = u
    else:
        p = random.randint(60, SCREEN_HEIGHT // 2)
        BUILDING.append(p)
        o += 1
if len(BUILDING) % 2 != 0:
    BUILDING.append(random.randint(60, SCREEN_HEIGHT // 2))

for i in range(len(BUILDING)-2):
    if i % 2 == 0:
        new_tuple = (BUILDING[i], BUILDING[i+1], BUILDING[i+2])
    elif i % 2 != 0:
        continue
    BUILDING_TUPLE.append(new_tuple)