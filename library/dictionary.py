''' Creation Date: 13/11/2022 '''

import json


# NOTE: Credit where credit is due, slumbers is adapted from Harry Cummings
# https://github.com/hgcummings/pixel-fonts


class Symbols:
    ''' Purpose: Creates object for all JSON pixel letters. '''
    def __init__(self, data: json):
        self.data = dict(data)
        self.allowed = set(data.keys())
    def get_coords(self, key: str, loc: list):
        ''' Returns: Width plus x, and y coordinates for key. '''
        pixels = self.data[key]
        x, y = [], []
        for y_index, array in enumerate(pixels[::-1]):
            for x_index, item in enumerate(array):
                if item != 0:
                    x.append(loc[0] + x_index)
                    y.append(loc[1] + y_index)
        return {'width': len(pixels[0]), 'x': x, 'y': y}


data = json.load(open("library/slumbers.json"))
x = Symbols(data)
print(x.get_coords('K', [1,1]))
print(x.get_coords('A', [5,1]))