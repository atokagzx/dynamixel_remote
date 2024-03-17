from setuptools import setup

setup(
    name="dynamixel-remote",
    version="0.0.1",
    description="Python library for controlling Dynamixel servos over BOLID C2000-eternet hub",
    author="Yaroslav Savelev",
    author_email="yaroslav21savelev@gmail.com",
    packages=["dynamixel_remote"],
    license="GNU Lesser General Public License v3",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: System :: Hardware :: Hardware Drivers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ])
