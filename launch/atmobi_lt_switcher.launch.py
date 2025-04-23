import os

import yaml
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    is_sim_mode_arg = DeclareLaunchArgument(
        'is_sim_mode',
        default_value='false',
        description='switch sim mode.'
    )

    headless = DeclareLaunchArgument(
        'headless',
        default_value='true',
        description='disable gui.'
    )

    config_file_color = os.path.join(get_package_share_directory(
        'swd_lt'), 'param_files', 'color_parameter.yaml')
    config_file_pid = os.path.join(get_package_share_directory(
        'swd_lt'), 'param_files', 'pid_parameter.yaml')
    with open(config_file_color, 'r') as f:
        configuration_color = yaml.safe_load(f)
        lower_h = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["lower_h"]
        lower_s = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["lower_s"]
        lower_v = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["lower_v"]
        upper_h = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["upper_h"]
        upper_s = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["upper_s"]
        upper_v = configuration_color["/swd_lt_line_recognition"]["ros__parameters"]["upper_v"]
    with open(config_file_pid, 'r') as f:
        configuration_pid = yaml.safe_load(f)
        control_p = configuration_pid["/swd_lt_controller"]["ros__parameters"]["control_p"]
        control_i = configuration_pid["/swd_lt_controller"]["ros__parameters"]["control_i"]
        control_d = configuration_pid["/swd_lt_controller"]["ros__parameters"]["control_d"]
        normal_speed_ms = \
            configuration_pid["/swd_lt_controller"]["ros__parameters"]["normal_speed_ms"]
        slow_speed_ms = \
            configuration_pid["/swd_lt_controller"]["ros__parameters"]["slow_speed_ms"]
        control_position_offset_cm = \
            configuration_pid["/swd_lt_controller"]["ros__parameters"]["control_position_offset_cm"]

    return LaunchDescription([
        is_sim_mode_arg,
        headless,

        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='v4l2_camera_node',
            parameters=[{'video_device': "/dev/swd-lt-camera",
                         'white_balance_temperature_auto': True,
                         'exposure_auto': 1,
                         'focus_auto': True,
                         'focus_absolute': 40}],
            remappings=[('/image_raw', '/camera/image_raw')],
            respawn=True,
            output='screen',
            condition=UnlessCondition(LaunchConfiguration('is_sim_mode'))
        ),
        Node(
            package='swd_lt',
            executable='swd_lt_aruco_maker_recognition',
            name='swd_lt_aruco_maker_recognition',
            parameters=[{'marker_size_m': 0.05,
                         'threshold_to_activate_r_marker': 0.0}],
            remappings=[('/image_raw', '/camera/image_raw')],
            output='screen'
        ),
        Node(
            package='swd_lt',
            executable='swd_lt_line_recognition',
            name='swd_lt_line_recognition',
            parameters=[{'min_area_size': 4000,
                        'lower_h': lower_h,
                         'lower_s': lower_s,
                         'lower_v': lower_v,
                         'upper_h': upper_h,
                         'upper_s': upper_s,
                         'upper_v': upper_v,
                         'line_lost_judgement_count': 20,
                         'headless': LaunchConfiguration('headless'),
                         }],
            remappings=[('/image_raw', '/camera/image_raw')],
            output='screen'
        ),
        Node(
            package='swd_lt',
            executable='swd_lt_controller',
            name='swd_lt_controller',
            parameters=[{'normal_speed_ms': normal_speed_ms,
                        'slow_speed_ms': slow_speed_ms,
                         'control_position_offset_cm': control_position_offset_cm,
                         'control_p': control_p,
                         'control_i': control_i,
                         'control_d': control_d}],
            output='screen'
        ),
        # Launch the "ros2bridge_websocket" node for topic communication with Node-RED
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='ros2bridge_websocket',
            parameters=[{
                'port': 9091  # custom port settings for rosbridge_websocket
            }],
            output='screen'
        ),
    ])
