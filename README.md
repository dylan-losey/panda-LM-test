# LM-Updates

Internal code for testing versions of LM control for robot arms

## Main Updates

- modified robot URDF files to increase the workspace
- added new functions (skills) for different types of grasps and grasp angles
- iteratively modified prompt through trial and error
- added ability to take initial image of environment, can use with VLM

## What's Missing?

- the commands are often very close to correct, but still need minor tweaks
- images are simulated, and may not be realistic enough to work perfectly
- want to incorporate a knowledge base to add skills / feedback associated with keywords
- target tasks: "put the cube in the drawer," "put the cube in the microwave"

## Install and Run

```bash

# Download
git clone https://github.com/dylan-losey/panda-LM-test
cd panda-LM-test

# Create and source virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install numpy pybullet matplotlib

# Run the script
python main.py
```

## Prompts

I provide two prompts. Really it is the same thing, but `prompt-with-image.txt` has some additional text and commands if you want to provide the image of the scene within the conversation.