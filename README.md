Robots on Asteroid

Documentation:

Please use pip install requirements.txt to 
install needed libraries.

App is using Flask - web framework to 
send final output to api endpoint.

robot.txt - contains input data from satellite. 
You can change file name, you will have 
to change variable name in app.py "file".

cls.py: file contains classes Asteroid and Robot.

Asteroid is class for new asteroid, 
contains scope of calculations. Robot - class 
for robot. Contains positions and methods: 
check_position - checking is robot is still in 
scope move_on - method is calling when robot moves

app.py file: contains operational functions: 
index - Flask function: var file - name of text file with input
        var file - name of text file with input
        
        13 and 14 opening file and reading line by line
        
        16-21 extraction data to json in list
        
        23-25 helping variables
        
        26-35 main loop reconizing inputs,
        creationg objects (Asteroid and Robots) and 
        doing methods 
        
        37-38 helping variables
        
        39-45 creating dict with output for sending to api
       
        48-49 Flask method



