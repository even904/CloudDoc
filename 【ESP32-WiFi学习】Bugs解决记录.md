---
author: [Even]
date: [2024年12月30日]
update: [2024年12月30日]
title: [【ESP32-WiFi学习】Bugs解决记录]
tags: [ESP32, FlashDownload, ESP-IDF]
---

# 概述
> 本文档说明使用ESP-IDF开发时遇到的Bugs及解决方法。

- [概述](#概述)
  - [FlashDownloadFailed](#flashdownloadfailed)

## FlashDownloadFailed
> 使用串口烧录失败
> 
> 应用解决：✅
> 问题复现：❎
> 逻辑解决：❓

上次烧录例程为ESP32的WiFi AP例程。
报错核心信息如下：
```
A fatal error occurred: No serial data received
```
1. 根据报错使用vofa检查串口，没有收到该串口发送的数据。
2. 插拔数据线后启动串口，更换USB口后启动串口，问题依然存在
3. 查询[ESP32 Troubleshooting](https://docs.espressif.com/projects/esptool/en/latest/esp32/troubleshooting.html)，猜测可能是板载CP2102损坏
    - ESP下载串口号为UART0，从引出的串口引脚TX0(GPIO1)和RX0(GPIO3)连接外部CH340，检查是否有数据输出。
    - 有数据输出，但一直重复输出，ESP32反复启动，猜测为CH340供电不稳
    - 尝试直接烧录，猜测由于反复启动，串口被占用，无法烧录
    - 连接USB数据线同时供电，尝试烧录，CH340回发数据显示正在等待烧录
    - 使用板载CP2102烧录，成功
4. 结论： CP2102未损坏，可能为供电电压不稳定引起CP2102停止工作，因此也引发CH340反复重启，临时解决方法是使用外部USB供电及对板载3.3V同时供电。


5. 后续： 当显示如下警告时
```--- Warning: GDB cannot open serial ports accessed as COMx
--- Using \\.\COM6 instead...
--- esp-idf-monitor 1.5.0 on \\.\COM6 115200
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H
```
重新插拔USB数据线可以正常接收数据及启动烧录。



