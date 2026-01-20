# panda-LM-test
internal code for testing LM robot control

## updates

- fixed move_to_pose so the robot actually goes where it is supposed to
	[solution was to remove internal collisions and joint limits, fine for simulation]
- updated the prompt and settings in qwen to remove internal memory
	[settings changed to reflect this, can delete chats occationally to make sure]

- TO DO: revise prompt using feedback from QWEN
	- maybe try on chatgpt as well?