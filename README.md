# BlackCow
Robots on Asteroid

Documentation:

Please use pip install requirements.txt to insall 
needed liberies.

App is using Flask - web framework to send final 
output to api endpoint. 

robot.txt - containes input data from satelite. 
You can change file name, you will have to change variable name 
in app.py "file". 

cls.py:
file contains classes Asteroid and Robot. 

Asteroid is class for new asteroid, containes scope of 
calculations.
Robot - class for robot. Containes positions and methods:
check_position - checking is robot is still in scoupe
move_on - method is calling when robot moves

app.py file:
containes operationals functions:
    index - Flask function:
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



