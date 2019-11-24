# FrontierHacks19: Humanoid
Laksh Bhambhani, Claire Chen, Nicholas Ng, Janhavi Singhal

## Inspiration

As members of FRC team 670, the idea of making this platform was inspired in part by our experiences in robotics, both with learning and teaching. A source of inspiration was Boston Dynamics' humanoid robots, while we also considered designs and challenges that we faced when we built our 2019 competition robot. 

## What it does

It has 2 arms and 2 legs with servo motors on the joints. Motion of these subsystems is controlled through Python code, and the robot can be easily programmed to do actions like walking, lifting and moving its arms, and dancing; this platform can be adapted by the user to be as simple or complex as they'd like.

## How we built it

Parts for the arm were designed using Fusion360 and 3d printed on a Monoprice printer. All the servos are controlled with a raspberry  pi through a 16 channel board from Adafruit. A lot of time was spent tuning values for how much the parts of the robot should move in a balanced way. Coding was done in Python; control from a server and the pi can be accessed from a webpage.

## Challenges we ran into

- Tuning values for balance to move everything how we want
- Mechanical challenges: making sure no parts are loose, everything fits well
- Being able to hold weight with the servos
- Original plan of coding in Java failed because it relied on a confusing library

## Accomplishments that we're proud of

- Our robot can dance!
- All subsystems work together and move

## What we learned

- Two of our team members were new to programming, but through working on this project learned to code in Python
- Integrating a mechanical and software system
- Designing and prototyping
