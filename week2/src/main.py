#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
from week2.srv import rad_ang_speed
from geometry_msgs.msg import Twist
def callback(rad):
    rospy.wait_for_service('compute_ang_vel')
    ang_speed = rospy.ServiceProxy('compute_ang_vel', rad_ang_speed)
    pub=rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    val=Twist()
    val.linear.x=0.2
    angular_speed=ang_speed(radius=rad.data)
    val.angular.z=angular_speed.ang_speed
    pub.publish(val)
rospy.init_node('main')
sub=rospy.Subscriber('radius', Float32, callback)
rospy.spin()