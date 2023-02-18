from robot_control_class import RobotControl
import time

# rc = RobotControl()


class square:
    def __init__(self, time, robot_speed, laser, laser2, laser3, dirc, ang):
        self.rc = RobotControl()
        self.robot_time = time
        self.speed = robot_speed
        self.Laser = laser
        self.Laser2 = laser2
        self.Laser3 = laser3
        self.direction = dirc
        self.angle = ang

    def do_square(self):
        while True:
            distance = self.rc.get_laser(self.Laser)
            print(distance)
            if distance < 0.8:
                self.stop()
            else:
                self.move1()

    def stop(self):
        self.rc.stop_robot()
        self.direction = 0
        self.angle = 90
        distance2 = self.rc.get_laser(self.Laser2)
        distance3 = self.rc.get_laser(self.Laser3)
        if distance2 < distance3:
            self.direction = 1
        if (self.direction) == 1:
            self.angle = -90
        self.turn()

    def move1(self):
        self.rc.move_straight()

    def turn(self):
        self.rotate()

    def rotate(self):
        self.rc.rotate((self.angle)-10.3)


ray = 360
ray2 = 0
ray3 = 719
angle = 90
speed = 0.4
time = 3.8
direction = 0

j1 = square(time, speed, ray, ray2, ray3, direction, angle)
j1.do_square()
