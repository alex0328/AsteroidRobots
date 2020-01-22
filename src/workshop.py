import json
import requests
from cls import Asteroid, Robot

file = open('robot.txt', 'r')
syp = file.read()

with open('robot.txt') as f:
    content = f.readlines()



asteroid_list = []
robots_list = []
for i in range(0, len(content)):
    pp = json.loads(content[i])
    if pp["type"] == "asteroid":
        r = requests.get('https://www.uuidgenerator.net/api/guid')
        asteroid_id = r.text
        ast = Asteroid(pp["size"]["x"], pp["size"]["y"], asteroid_id)
        asteroid_list.append(ast)
    elif pp["type"] == "new-robot":
        robot = Robot(pp["position"]["x"],pp["position"]["y"],pp["bearing"], ast.asteroid_id)
        robots_list.append(robot)
    elif pp["type"] == "move":
        pass

print(asteroid_list)
print(robots_list)







# y = json.loads(content[3])
# print(y)



#json_file = '{ "name":"John", "age":30, "city":"New York"}'
#python_object = json.load(json_file)











