#!/usr/bin/env python3
from study_pkg.srv import PolyArray, PolyArrayResponse
import rospy
from std_msgs.msg import String
from study_pkg.msg import Array_int64



#тело программы
def start_summator(req):
	msg = String()
	result = 0
	for i in range(len(req.elements)):
		result = result + (req.elements[i] ** (len(req.elements) - i))
	rospy.loginfo('summator is summing: %s' % result)
	msg.data = str(result)
	pub.publish(msg)
		
		
rospy.init_node('summator')
pub = rospy.Publisher('from_summator', String, queue_size=10)
rospy.Subscriber('to_summator', Array_int64, start_summator, queue_size=10)
rospy.spin()
