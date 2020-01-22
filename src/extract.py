import json
from cls import Asteroid, Robot
#
# file = open('robot.txt', 'r')
# syp = file.read()

with open('robot.txt') as f:
    content = f.readlines()

def extract_data(content):
    change = 0
    move = 0
    robots = []
    alle = []
    for i in range(0, len(content)):
        pp = json.loads(content[i])
        if pp["type"] == "move":
            pp["robot_id"] = change
            move = move +1
            pp["move_nr"] = move
            robots.append(pp)
        if pp["type"] == "new-robot":
            move = 0
            change = change + 1
        alle.append(pp)
    return alle



direction = ["turn-left", "turn-right", "move-forward"]
asteroid_nr = 1
robot_nr = 1
robots_obj = []
count = 1
for i in extract_data(content):
    if i["type"] == "asteroid":
        asteroid = Asteroid(i["size"]["x"], i["size"]["y"], asteroid_nr)
        asteroid_nr = asteroid_nr + 1
        #print(asteroid)
    if i["type"] == "new-robot":
        robot = Robot(i["position"]["x"], i["position"]["y"], i["bearing"], robot_nr, asteroid_nr)
        robots_obj.append(robot)
        robot_nr = robot_nr + 1
        #print(robots_obj)
    if i["type"] == "move":
        #print("count = {}".format(count))
        count = count + 1
        robot.move_on(i["movement"])
    #     print(robot.position_x)
    #     print(robot.bearing)
    # print(robots_obj)


output = {}
for i in robots_obj:
    output["type"] = "robot"
    position = {"x": i.position_x, "y": i.position_y}
    output["position"] = position
    output["bearing"] = i.bearing
    print(output)

























