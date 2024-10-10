from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'robot_timed_forward'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        #(os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', 'launch.[pxy][yma]'))),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='egutierrezcornejo',
    maintainer_email='emanuelgtz02@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = robot_timed_forward.timed_forward_pub:main',
        ],
    },
)
