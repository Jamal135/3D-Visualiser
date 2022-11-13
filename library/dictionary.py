''' Creation Date: 13/11/2022 '''

import json


# NOTE: Credit where credit is due, slumbers is adapted from Harry Cummings
# https://github.com/hgcummings/pixel-fonts


class Symbols:
    ''' Purpose: Creates object for all JSON pixel letters. '''
    def __init__(self, data):
        chars = data.keys()
        for key in chars:
            _pixels = data[key]
            setattr(self, key, _pixels)
        self.allowed = set(chars)
    def get_coords(self, key, loc: dict = {'x': 1, 'y': 1}):
        ''' Returns: Width plus x, and y coordinates for key. '''
        pixels = getattr(self, key)
        x, y = [], []
        for y_index, array in enumerate(pixels[::-1]):
            for x_index, item in enumerate(array):
                if item != 0:
                    x.append(loc['x'] + x_index)
                    y.append(loc['y'] + y_index)
        return {'width': len(pixels[0]), 'x': x, 'y': y}


data = json.load(open("library/slumbers.json"))
x = Symbols(data)
print(x.get_coords('K', {'x': 1, 'y': 1}))
print(x.get_coords('A', {'x': 5, 'y': 1}))