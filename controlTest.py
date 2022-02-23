#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String



if __name__ == '__main__':
    pub = rospy.Publisher('/tello/cmd_vel', String, queue_size=10)
    rospy.init_node('controller', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()
