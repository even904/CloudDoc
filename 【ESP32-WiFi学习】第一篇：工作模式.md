---
author: [Even]
date: [2024年12月29日]
update: [2024年12月30日]
title: [【ESP32-WiFi学习】第一篇：工作模式]
tags: [ESP32,WiFi,ESP-IDF]
---

# 【ESP32-WiFi学习】第一篇：工作模式

## 概述
> -   station 模式（即 STA 模式或 Wi-Fi 客户端模式），此时 ESP32 连接到接入点 (AP)。
> 
> -    AP 模式（即 Soft-AP 模式或接入点模式），此时基站连接到 ESP32。
> 
> -    station/AP 共存模式（ESP32 既是接入点，同时又作为基站连接到另外一个接入点）。
> 
> -    上述模式的各种安全模式（WPA、WPA2、WPA3 等）。
> 
> -    扫描接入点（包括主动扫描及被动扫描）。
> 
> -    使用混杂模式监控 IEEE802.11 Wi-Fi 数据包。

## ESP32支持的WiFi工作模式
### Station模式
此时ESP32连接到接入点 (AP)。可以使用ESP32连接到WiFi，从而接入互联网。

### AP模式
AP模式类似于家用路由器的工作模式，使得其他Wi-Fi设备可以像连接到普通路由器一样连接到这个设备。如果ESP32本身接入了Ethernet从而可以提供互联网访问，则其他设备接入后可通过该网络上网，否则就只是接入了一个局域网。

ESP32没有没有独立的、专门针对AP功能优化的硬件组件，因此使用Soft AP，Soft AP允许设备通过软件配置来充当Wi-Fi接入点。

为ESP32配置Soft AP模式，在ESP-IDF工具链中，需要修改`MenuConfig`中的`WiFi SSID`及`WiFi Password`，从而设置ESP32提供的AP的名称和密码。ESP-IDF编译时将提取配置信息，写入代码中。



![img](https://eleceasy.com/uploads/default/optimized/2X/e/eef38b615678f67215f5f275334c357fba3b7a78_2_1024x576.jpeg)**AP与STA模式** *(图源：https://eleceasy.com)*

## Debug

