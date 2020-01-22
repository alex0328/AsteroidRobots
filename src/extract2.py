import json
from cls import Asteroid, Robot


with open('robot.txt') as f:
    content = f.readlines()

def extract_data(content):
    alle = []
    for i in range(0, len(content)):
        pp = json.loads(content[i])
        alle.append(pp)
    return alle

asteroid_nr = 1
robot_nr = 1
robots_obj = []
for i in extract_data(content):
    if i["type"] == "asteroid":
        asteroid = Asteroid(i["size"]["x"], i["size"]["y"], asteroid_nr)
        asteroid_nr = asteroid_nr + 1
    elif i["type"] == "new-robot":
        robot = Robot(i["position"]["x"], i["position"]["y"], i["bearing"], robot_nr, asteroid_nr)
        robots_obj.append(robot)
        robot_nr = robot_nr + 1
    elif i["type"] == "move":
        robot.move_on(i["movement"])

output = {}
for i in robots_obj:
    output["type"] = "robot"
    position = {"x": i.position_x, "y": i.position_y}
    output["position"] = position
    output["bearing"] = i.bearing
    print(output)

