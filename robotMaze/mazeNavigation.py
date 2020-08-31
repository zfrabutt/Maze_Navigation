from robot_control_class import RobotControl
import math

class robotMaze:
    def __init__(self, moveDirection, turnDirection, speed):
        self.RobotControl = RobotControl()
        self.moveDirection = moveDirection
        self.turnDirection = turnDirection
        self.speed = speed
        self.timeTurn = 4.80 #Set to get as close to 90 degrees as possible
        self.left = 0 #Sets leftmost laser value
        self.middle = 360 #sets middle laser value
        self.right = 719 #sets rightmost laser value

    def solveMaze(self):
        

        while ((self.RobotControl.get_laser(self.left) != math.inf) & (self.RobotControl.get_laser(self.right) != math.inf)):
            self.wallMove()
            self.checkBounds()

        self.RobotControl.move_straight()
        self.RobotControl.stop_robot()

    def wallMove(self):

        distance = self.RobotControl.get_laser(self.middle)

        while (distance > 1) :
            self.RobotControl.move_straight()
            distance = self.RobotControl.get_laser(self.middle)
        
        self.RobotControl.stop_robot()

    def checkBounds(self):
        leftSide = self.RobotControl.get_laser(self.left)
        rightSide = self.RobotControl.get_laser(self.right)

        if (leftSide > rightSide):
            self.turnDirection = 'clockwise'
            self.RobotControl.turn(self.turnDirection, self.speed, self.timeTurn)
        else:
            self.turnDirection = 'counter-clockwise'
            self.RobotControl.turn(self.turnDirection, self.speed, self.timeTurn)

mazeRob1 = robotMaze('forward', 'clockwise', .3)
mazeRob1.solveMaze()