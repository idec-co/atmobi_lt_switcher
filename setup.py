import os
from glob import glob
from setuptools import setup

package_name = 'atmobi_lt_switcher'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='IDEC Corporation',
    maintainer_email='zz_gitadmin@idec.com',
    description='This is a package that works with the swd_lt to improve atmobi accuracy.',
    license='LGPLv2.1',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
