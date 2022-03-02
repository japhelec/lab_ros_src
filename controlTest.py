#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Empty
from threading import Timer


## register node
topic_cmd = rospy.Publisher('/tello/cmd_vel', Twist, queue_size=1)
topic_takeoff = rospy.Publisher('/tello/takeoff', Empty, queue_size=1)
topic_land = rospy.Publisher('/tello/land', Empty, queue_size=1)

rospy.init_node('control_test', anonymous=True)

## takeoff
empty = Empty()
topic_takeoff.publish(empty)
rate = rospy.Rate(10) # 10hz

## prepare message
### stop
msg0 = Twist()
msg0.linear.x = 0
msg0.linear.y = 0
msg0.linear.z = 0

### test
msg1 = Twist()
msg1.linear.z = 1
msg2 = Twist()
msg2.linear.x = 1
msg3 = Twist()
msg3.linear.y = 1



def control():
    ## control!
    counter = 0

    while not rospy.is_shutdown():
        counter += 1


        if counter <= 20:
            msg = msg0
            topic_cmd.publish(msg)
            rate.sleep()
            continue

        # if counter < 10:
        #     msg = msg1
        #     topic_cmd.publish(msg)
        #     rate.sleep()
        #     continue

        # elif counter == 10:
        #     msg = msg0
        #     topic_cmd.publish(msg)
        #     rate.sleep()
        #     continue        
        
        else: 
            # msg = msg0
            # pub.publish(msg)
            topic_land.publish(empty)
            break
    
    topic_land.publish(empty)
    rospy.signal_shutdown("control terminated")




t = Timer(5.0, control)
t.start()


