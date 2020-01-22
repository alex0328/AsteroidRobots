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
    def __init__(self, position_x, position_y, bearing, robot_id, asteroid):
        self.position_x = position_x
        self.position_y = position_y
        self.bearing = bearing
        self.robot_id = robot_id
        self.asteroid = asteroid

    def check_position(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        if self.position_x > self.max_x or self.position_y > self.max_y:
            return ('Smth goes wrong - Robot out of scoupe')
        return ("position is ok")

    def move_on(self, direction):
        if direction == "turn-left":
            if self.bearing == "north":
                self.position_x -= 1
                self.bearing = "west" #1
            elif self.bearing == "south":
                self.position_x += 1 #11
                self.bearing = "east"
            elif self.bearing == "east":
                self.position_y += 1
                self.bearing = "north" #111
            elif self.bearing == "west":
                self.position_y -= 1
                self.bearing = "south"
        elif direction == "turn-right":
            if self.bearing == "north":
                self.position_x += 1
                self.bearing = "east" #22
            elif self.bearing == "south":
                self.position_x -= 1
                self.bearing = "west" #2
            elif self.bearing == "east":
                self.position_y -= 1
                self.bearing = "south"
            elif self.bearing == "west":
                self.position_y += 1
                self.bearing = "north" #222
        elif direction == "move-forward":
            if self.bearing == "north":
                self.position_y += 1 #333
            elif self.bearing == "south":
                self.position_y -= 1
            elif self.bearing == "east":
                self.position_x += 1 #33
            elif self.bearing == "west":
                self.position_x -= 1 #3
