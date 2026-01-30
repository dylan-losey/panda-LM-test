import math

# Simulation
control_dt = 1. / 240.

# Robot
baseStartPosition = [0.0, 0.0, 0.0]
baseStartOrientationE = [0.0, 0.0, 0.0]
jointStartPositions = [0.0, 0.0, 0.0, -2*math.pi/4, 0.0, math.pi/2, math.pi/4, 0.0, 0.0, 0.04, 0.04]

# GUI Camera
cameraDistance = 1.0
cameraYaw = 40.0
cameraPitch = -30.0
cameraTargetPosition = [0.5, 0.0, 0.2]

# External Camera
ext_cameraDistance = 0.7
ext_cameraYaw = -90
ext_cameraPitch = -40
ext_cameraTargetPosition = [0.7, 0, 0.2]