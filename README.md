# panda-LM-test
internal code for testing LM robot control

## updates

- fixed move_to_pose so the robot actually goes where it is supposed to
	- now follows a very long trajectory in joint space?
	- removed collision on most links of the end-effector	
	- make a virtual robot that only has the gripper? The joints are xyz concentric followed by wrist concentric?
- updated the prompt and settings in qwen to remove internal memory [double check this?]

- revised prompt to improve consistency
- i think we can use qwen to try and improve the prompt.