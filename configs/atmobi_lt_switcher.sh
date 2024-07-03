#!/bin/bash

set -e

DIR=/home/atmobi/ros2_ws/install

# Check if ROS Foxy is installed
if [ -f "/opt/ros/foxy/setup.bash" ]; then
    # Source ROS Foxy setup.bash
    source /opt/ros/foxy/setup.bash
    echo "ROS Foxy environment set up."
else
    echo "Error: ROS Foxy not found in $/opt/ros/foxy."
    echo "Make sure ROS Foxy is installed and the setup.bash file exists."
    exit 1
fi

# Check if ROS 2 workspace setup script is available
if [ -f "${DIR}/setup.bash" ]; then
    # Source ROS 2 workspace setup.bash
    source ${DIR}/setup.bash
    echo "ROS 2 workspace environment set up."
else
    echo "Error: ROS 2 workspace setup script not found in ${DIR}/setup.bash."
    echo "Make sure your ROS 2 workspace is built and the setup.bash file exists."
    exit 1
fi

# launch atmobi_lt_switcher_service_launch.py
ros2 launch atmobi_lt_switcher atmobi_lt_switcher.launch.py
