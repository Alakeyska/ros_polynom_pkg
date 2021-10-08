#!/usr/bin/env python3
from study_pkg.srv import PolyArray, PolyArrayResponse, PolyArrayRequest
from study_pkg.msg import Array_int64
from std_msgs.msg import String
import rospy

def callback(answer):
	rospy.loginfo('i came from summator %s' % answer.data)
	resp.poly = int(answer.data)


def hande_poly_srv(req):
	returning_string = ''
	for i in range(len(req.coeff)):
		if i != (len(req.coeff) - 1) :
			returning_string += str(req.coeff[i]) + '^' + str((len(req.coeff) - i)) + ' + '
		else:
			returning_string += str(req.coeff[i])
	pub.publish(req.coeff)
	
	#rate.sleep()
		
	resp.instr = returning_string
	rospy.loginfo("Returning %s = %s" % (returning_string, resp.poly))
	rospy.loginfo("------------------------")
	return resp

	
def poly_server():
	s = rospy.Service('poly', PolyArray, hande_poly_srv)
	rospy.loginfo('Ready to calc')
	rospy.spin()


rospy.init_node('poly_server')
pub = rospy.Publisher('to_summator', Array_int64, queue_size = 10)
rate = rospy.Rate(1)

rospy.Subscriber('from_summator', String, callback, queue_size = 10)

resp = PolyArrayResponse()
poly_server()

