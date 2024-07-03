#!/bin/bash

set -e

# Check if ROS Noetic is installed
if [ -f "/opt/ros/noetic/setup.bash" ]; then
    # Source ROS Noetic setup.bash
    source /opt/ros/noetic/setup.bash
    echo "ROS Noetic environment set up."
else
    echo "Error: ROS Noetic not found in /opt/ros/noetic."
    echo "Make sure ROS Noetic is installed and the setup.bash file exists." >&2
    exit 1
fi

# Check if ROS Foxy is installed
if [ -f "/opt/ros/foxy/setup.bash" ]; then
    # Source ROS Foxy setup.bash
    source /opt/ros/foxy/setup.bash
    echo "ROS Foxy environment set up."
else
    echo "Error: ROS Foxy not found in /opt/ros/foxy."
    echo "Make sure ROS Foxy is installed and the setup.bash file exists." >&2
    exit 1
fi

# Add ROS 1 and ROS 2 library paths to LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/opt/ros/noetic/lib:/opt/ros/foxy/lib

# Start dynamic_bridge
ros2 run ros1_bridge dynamic_bridge
