# Attach to container shell
```
docker exec -it ta_create3 bash
```

# Refresh bash environment & start fastdds server inside docker container
```
source ~/.bashrc
fastdds discovery -i 0 -l 192.168.186.3 -p 11811
```

# Run timed movement script
```
source ~/create3_ws/install/setup.bash
ros2 run robot_timed_forward publisher
```
# Launch movement script with ros launch

```
source ~/create3_ws/install/setup.bash
ros2 launch robot_timed_forward timed_forward.launch.py
```

# Run xbox controller movement script (use X + direction to move)
```
ros2 launch teleop_twist_joy teleop-launch.py joy_config:='xbox'
```
