#!/usr/bin/env python3
import rospy
from study_pkg.srv import PolyArray, PolyArrayRequest, PolyArrayResponse
from study_pkg.msg import Array_int64
import sys

def poly_clients (lst):
	rospy.wait_for_service('poly')
	try:
		poly_srv = rospy.ServiceProxy('poly', PolyArray)
		req = PolyArrayRequest (lst)
		resp = poly_srv(req)
		
		print('Response: %s = %s' % (resp.instr, resp.poly))
		rospy.loginfo('Response: %s' % resp.poly)
	except (rospy.ServiceException):
		rospy.logerr('Service call failed: %s')
	
if len(sys.argv) >= 1:
	i = 1
	input_str = []
	while i < len(sys.argv):
		input_str.append(int(sys.argv[i]))
		i += 1
	poly_clients (input_str)
else:
	print('enter arguments')
	sys.exit(1)



