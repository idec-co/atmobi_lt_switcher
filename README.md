atmobi_lt_switcher
===============

# Overview
The system switches from `@mobi` navigation to line guidance, detects AR markers at the destination, and stops the AMR.  
This system stops with better accuracy than `@mobi` by itself.

**This package requires `@mobi` a software package for autonomous mobile robots from Panasonic Advanced Technology Co., Ltd.**

# Prerequisites
- Ubuntu 20.04
- ROS2 Foxy

# Dependent Packages
- Set up `EZW-CUBE` according to the **EZW-CUBE_簡易マニュアル(ソフトウェア).pdf**.
- Set up `swd_lt` package according to **SWDスターターキット_ライントレースプログラム_ユーザーズマニュアル.pdf**.
- Install other dependent ROS2 packages:
```
sudo apt install ros-foxy-ros1-bridge ros-foxy-rosbridge-suite
```

# Usage
1. Launch atmobi with EZW-CUBE.
1. Launch `swd_lt` and `rosbridge_server`.
```
bash atmobi_lt_switcher.sh
```
3. Launch `ros1_bridge`.
```
bash ros1_bridge.sh
```
