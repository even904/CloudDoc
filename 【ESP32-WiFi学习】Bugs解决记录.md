---
author: [Even]
date: [2024年12月30日]
update: [2025年01月08日]
title: [【ESP32-WiFi学习】Bugs解决记录]
tags: [ESP32, FlashDownload, ESP-IDF]
---

# 概述
> 本文档说明使用ESP-IDF开发时遇到的Bugs及解决方法。

- [概述](#概述)
  - [FlashDownloadFailed](#flashdownloadfailed)
  - [OOM](#oom)
  - [LVGL `lv_disp_set_rotation(disp_handle, LV_DISPLAY_ROTATION_90)` 失败并卡死](#lvgl-lv_disp_set_rotationdisp_handle-lv_display_rotation_90-失败并卡死)

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

```
--- Warning: GDB cannot open serial ports accessed as COMx
--- Using \\.\COM6 instead...
--- esp-idf-monitor 1.5.0 on \\.\COM6 115200
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H
```
重新插拔USB数据线可以正常接收数据及启动烧录。

## OOM
> 使用VSCode ESP-IDF插件，运行预定义的任务(Tasks)，如打开组件管理器、下载第三方组件（如LVGL等）、编译、切换芯片类型等时发生内存溢出问题。这将导致系统界面崩溃、程序重启、黑屏等各种现象。
>
> 应用解决：✅
> 问题复现：✅
> 逻辑解决：❎

系统日志如下：
![](https://raw.githubusercontent.com/even904/Images/main/pic/application-crash.png)

解决方法：
- 增大虚拟内存(Swap)
Windows下可以通过`此电脑-属性-调整Windows的外观和性能-高级`对虚拟内存进行拓展，能一定程度上解决硬件内存不足的问题。

![](https://raw.githubusercontent.com/even904/Images/main/pic/20250106224753.png)

- 除编译外，尚未对ESP-IDF的行为进行分析，因此不知道OOM的具体原因。需要注意，在项目文件较多时无论打开配置还是下载第三方组件都可能导致ESP-IDF的内存溢出。


## LVGL `lv_disp_set_rotation(disp_handle, LV_DISPLAY_ROTATION_90)` 失败并卡死

> 使用VSCode ESP-IDF插件，运行预定义的任务(Tasks)，如打开组件管理器、下载第三方组件（如LVGL等）、编译、切换芯片类型等时发生内存溢出问题。这将导致系统界面崩溃、程序重启、黑屏等各种现象。
>
> 应用解决：✅
> 问题复现：✅
> 逻辑解决：❓

此问题大概率是因为传入指针disp_handle没有正确初始化导致的。当未传入正确初始化的指针时，系统不会输出错误LOG，而是直接卡死，导致此语句及之后语句均无法正常运行。

如果勾选了`Enable system monitor component`以自动显示FPS信息，若调用了本句，则可能导致无法正常显示，猜测原因可能也为指针未初始化。但由于将lvgl内部视作黑箱，暂时没有排查内部原因。排查思路应该为，分析lvgl绘制FPS显示窗口函数的调用栈，找出默认的传入指针参数，分析传入参数是否有误；分析lvgl绘制任务是否会影响disp_handle指针，尽管它已经被定义为`const`。

目前的解决方法：显示FPS信息时，不调用屏幕旋转函数；实际应用时，禁用`system monitor component`，可正常调用屏幕旋转函数。