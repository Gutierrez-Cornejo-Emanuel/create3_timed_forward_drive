from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='robot_timed_forward',
            executable='publisher',
            name='publisher',
            output='screen',
            prefix = 'xterm -e'
        )
    ])