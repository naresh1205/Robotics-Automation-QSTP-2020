#!/usr/bin/env python
import rospy
from week2.srv import rad_ang_speed, rad_ang_speedResponse, rad_ang_speedRequest
def ang_speed(request):
    return rad_ang_speedResponse(1.00/request.radius)
rospy.init_node('angular_server')
service=rospy.Service('compute_ang_vel', rad_ang_speed, ang_speed)
rospy.spin()
