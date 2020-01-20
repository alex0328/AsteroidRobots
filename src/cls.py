class Asteroid:
    def __init__(self, size_x, size_y, asteroid_id):
        self.size_x = size_x
        self.size_y = size_y
        self.asteroid_id = asteroid_id

    @property
    def get_size_x(self):
        return self.size_x

    @property
    def get_size_y(self):
        return self.size_y

class Robot:
    def __init__(self, position_x, position_y, bearing, asteroid):
        self.asteroid = asteroid
        self.position_x = position_x
        self.position_y = position_y
        self.bearing = bearing

    def check_position(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        if self.position_x > self.max_x or self.position_y > self.max_y:
            return ('Smth goes wrong - Robot out of scoupe')
        return ("position is ok")

    def move(self, turn):
        pass