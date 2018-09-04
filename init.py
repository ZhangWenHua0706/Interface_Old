# -*- coding:utf-8 -*-
from RobotLogin import RobotLogin
from RobotLogin2 import RobotLogin2
from RobotScroll import RobotScroll
version = '1.0'
class MyLogin(RobotLogin):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
class MyLogin1(RobotLogin2):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
class MyRobotScroll(RobotScroll):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'