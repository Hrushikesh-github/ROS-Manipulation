#! /usr/bin/env python

import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
'''
The most important one here is the moveit_commander module, which will allow us to communicate 
with the MoveIt RViz interface.
'''

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
#Here, we are just initializing the moveit_commander module.
robot = moveit_commander.RobotCommander()
#creating a RobotCommander object, which is, basically, an interface to our robot.
scene = moveit_commander.PlanningSceneInterface()
#Here, we are creating a PlanningSceneInterface object, which is, basically, 
#an interface to the world that surrounds the robot.
group = moveit_commander.MoveGroupCommander("arm")
#a MoveGroupCommander object, which is an interface to the manipulator group of joints that we defined when we created the MoveIt package, back in the Chapter 1. This will allow us to interact with this set of joints, which, in this case, is the full arm.
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory, queue_size=1)
#Here, we are defining a Topic Publisher, which will publish into the /move_group/display_planned_path topic. By publishing into this topic, we will be able to visualize the planned motion through the MoveIt RViz interface.
group_variable_values = group.get_current_joint_values()
group_variable_values[5] = -1.5
group.set_joint_value_target(group_variable_values)
 
plan2 = group.plan()

rospy.sleep(5)
#group.go(wait=True)
#In order to execute a trajectory for sim/real robot
moveit_commander.roscpp_shutdown()