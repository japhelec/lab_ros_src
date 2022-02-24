#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from threading import Timer


## register node
topic_cmd = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=1)
rospy.init_node('control_test', anonymous=True)

rate = rospy.Rate(10) # 10hz

## prepare message
### stop
msg0 = Twist()
msg0.linear.x = 0
msg0.linear.y = 0
msg0.linear.z = 0

### test
msg1 = Twist()
msg1.linear.z = 1 ## move upward
msg2 = Twist()
msg2.linear.x = 1 ## move to the right of marker B
msg3 = Twist()
msg3.linear.y = 1 ## move to the front of camera



def control():
    ## control!
    counter = 0

    while not rospy.is_shutdown():
        counter += 1


        if counter <= 15:
            msg = msg2
            topic_cmd.publish(msg)
            rate.sleep()
            continue     
        
        else: 
            msg = msg0
            topic_cmd.publish(msg)
            rate.sleep()
            continue

control()


