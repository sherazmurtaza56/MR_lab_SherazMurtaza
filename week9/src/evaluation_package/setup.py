import os
from glob import glob
from setuptools import setup

package_name = 'evaluation_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # This line allows ROS 2 to find your launch files
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sheraz',
    maintainer_email='sheraz@todo.todo',
    description='Autonomous Localization Recovery System for Mobile Robotics Evaluation',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # This links the command 'recovery_node' to your Python script
            'recovery_node = evaluation_package.marker_recovery:main',
        ],
    },
)
