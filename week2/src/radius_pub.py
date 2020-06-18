#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32
rospy.init_node('radius_pub')
pub=rospy.Publisher('radius', Float32, queue_size=10)
r=1.00
rate=rospy.Rate(1)
while not rospy.is_shutdown():
    pub.publish(r)
    rate.sleep()