''' Creation Date: 12/11/2022 '''

import plotly.graph_objects as go
import math


data =[[5,5,4,4,3,3,3,2,2,1,1,5,3,2,1], [1,3,1,3,1,2,3,1,3,1,3,5,5,5,5], [1,0,2,5,4,2,4,1,3,4,2,1,3,4,2]]
'ererer'
class Data:
    ''' Contains: Data lists for x, y, and z. '''
    def __init__(self, x: list, y: list, z: list):
        self.x = x
        ''' List of x coordinate integers. ''' 
        self.y = y 
        ''' List of y coordinate integers. '''
        self.z = z
        ''' List of z coordinate integers. '''
    def get_length(self):
        ''' Returns: Maxinum length of x, y, and z. '''
        return max(len(self.x), len(self.y), len(self.z))
    def get_data(self):
        ''' Returns: List of lists of x, y, and z. '''
        return [self.x, self.y, self.z]
    def __str__(self):
        return f"{str(self.__class__)}: {str(self.__dict__)}"


def circle_rotation(Coords: Data, rotation: int, horizontal: True):
    ''' Returns: Coordinates rotated to a point on a circle. '''
    radians = math.radians(rotation)
    cos = math.cos(radians)
    sin = math.sin(radians)
    x = Coords.x if horizontal else Coords.y # Vertical
    y = Coords.z
    for index in range(Coords.get_length()):
        rotated_x = round(x[index] * cos - y[index] * sin)
        rotated_y = round(y[index] * cos + x[index] * sin)
        if horizontal:
            Coords.x[index] = rotated_x
        else:
            Coords.y[index] = rotated_x
        Coords.z[index] = rotated_y
    return Coords


def spherical_rotation(Coords: Data, x_rotation: int, y_rotation: int):
    ''' Returns: Coordinates rotated to a point on a sphere. '''
    Coords = circle_rotation(Coords, x_rotation, True)
    return circle_rotation(Coords, y_rotation, False)


if __name__ == '__main__':
    Coords = Data(data[0], data[1], data[2])
    Coords = spherical_rotation(Coords, 0, 0)
    fig = go.Figure(data=[go.Scatter3d(
        x=Coords.x,
        y=Coords.y,
        z=Coords.z,
        mode='markers',
        marker=dict(
            size=12,
            opacity=0.8
        ))])
    camera = dict(
        eye=dict(x=0, y=0, z=-22)
    )
    fig.update_layout(
        scene_camera=camera
    )
    fig.update_scenes(
        camera_projection_type="orthographic",
        xaxis_visible=False,
        yaxis_visible=False,
        zaxis_visible=False 
    )
    
    fig.show()
