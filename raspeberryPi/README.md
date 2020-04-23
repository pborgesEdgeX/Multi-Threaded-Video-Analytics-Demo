# Raspberry-Pi Demo
Client Side (Raspberry Pi) Demo: Multi-threaded Analytics Flask based (Python) based code.

[![GitHub license](https://img.shields.io/github/license/pborgesEdgeX/paphack)](https://github.com/pborgesEdgeX/paphack/blob/master/LICENSE) [![GitHub issues](https://img.shields.io/github/issues/pborgesEdgeX/paphack)](https://github.com/pborgesEdgeX/paphack/issues) [![GitHub forks](https://img.shields.io/github/forks/pborgesEdgeX/paphack)](https://github.com/pborgesEdgeX/paphack/forks)  [![GitHub stars](https://img.shields.io/github/stars/pborgesEdgeX/paphack)](https://github.com/pborgesEdgeX/paphack/stargazers)

## Getting Started

These instructions provide you a copy of the project up and running on your raspberry pi W Zero for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For you to build this code successfully, make sure you have the following installed:

```
# Python 3.6
$ python3 --version
Python 3.6.5

If Python 3 not installed, then follow the instructions on 
```
* [Python3 Installation](https://samx18.io/blog/2018/09/05/python3_raspberrypi.html) - Installing Python 3 on RPI
```
$ pip3 --version
pip 19.1.1

$ virtualenv --version
16.7.2

```
### Tested Environment
Operating system:
* Raspberry: Raspbian Buster Lite (2020-02-13)
* Host: macOS Catalina 10.15.3

### Overall Architecture
With this demo, we are building a complete producer to consumer application for video streaming. We picked the sample video from the Raspberry pi Zero source via URL streamed via a Producer inside the Kafka network. The producer is written in Python to send frames to the Kafka pipe in the most efficient manner. Keep in mind some image resizing is needed to ensure the pipe doesn't overload.

### Installing

To get your code up and running, first let's clone the repo locally then compose the project:

```
$ cd /src/bin/
$ python3 main.py
```
If you don't have Python3 as in the default path of your bash profile, then activate the virtual environment by:

```
$ cd /src/bin/
$ source activate
$ python3 main.py
```

If you are running the script successfully, you should see the following output:

******************************************************
* This is the Video Stream Script,     *
******************************************************
******************************************************
******************************************************


## Running 

Once the system is up and running, you can see the consumers running on a Flask powered web-server.

The live stream can now be access from your network by: http://<RPI IP>:8000


## Troubleshooting
If you have any issues connecting to the raspberry via SSH, then try the following:

Step 1:
1) Identify the Raspberry Pi IP by using Lan Scan available at the App Store. If you don't see it in the home network then the Raspberry Pi is not connecting to your wifi.

2) If you are not seeing the connection, connect the microSD into your MAC, and follow these steps:

Open a terminal window:
```
$ cd /Volumes/boot
$ touch wpa_supplicant.conf
$ nano wpa_supplicant.conf
Copy and paste the following replacing NETWORK-NAME AND NETWORK-PASSWORD with the credentials of your home network: 
country=US
  ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
  update_config=1

  network={
      ssid="NETWORK-NAME"
      psk="NETWORK-PASSWORD"
  }

```

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - Consumer Web Server
* [OpenCV](https://docs.opencv.org/) - Computer Vision Library in Consumer

## Versioning

We use [SemVer](http://semver.org/) for versioning. The latest version of this code is 1.0.0.

## Authors

* **[Paulo Borges](https://www.linkedin.com/in/pborges1/)** - *Initial work* - [MobiledgeX](https://github.com/pborgesEdgeX)

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/pborgesEdgeX/full_app/blob/master/LICENSE) file for details

