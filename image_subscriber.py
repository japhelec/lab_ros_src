#!/usr/bin/env python

# used to test image collection 
# used to capture image for calibration
import cv2
from cv_bridge import CvBridge
import numpy as np
import rospy
from sensor_msgs.msg import Image

entry = 200
total_frame = 1680
picture_no = 40
interval = total_frame / picture_no

picture_id = 0
frame_id = 0
last_pictue = 0

def callback(ros_data):
    global frame_id
    global picture_id
    global last_pictue
    frame_id += 1

    if (frame_id > entry):
        if (frame_id - last_pictue > interval):
            picture_id += 1
            img = br.imgmsg_to_cv2(ros_data)
            cv2.imwrite('./pictures/picture_' + str(picture_id) + '.jpg', img)
            cv2.imshow('Test', img)
            cv2.waitKey(2)
            last_pictue = frame_id

def listener():
    rospy.init_node('image_subscriber', anonymous=True)
    rospy.Subscriber("/test", Image, callback, queue_size = 1)
    rospy.spin()

if __name__ == '__main__':
    br = CvBridge()  
    listener()

# rosrun image_transport republish h264 in:=/tello/image_raw raw out:=/test