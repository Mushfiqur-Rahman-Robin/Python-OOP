# named tuple is kind of lightweight object that works just like a regular tuple but its more readable  

from collections import namedtuple

color = (55, 155, 255)

color = {'red': 55, 'green': 155, 'blue': 255}

# named tuple
color = namedtuple('color', ['red', 'green', 'blue'])
color = color(blue = 55, green = 155, red = 255)

print(color.red)
