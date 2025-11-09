---
author: [Even]
date: [2025年10月28日]
update: [2025年10月28日]
title: [【计算机网络】实践-2：ssh跨网转发]
tags: [计算机网络, CVM, 端口转发]
---


``` sh
# 将连接到本机的 8080 端口的流量转发至 us.ddupan.top 的 8080 端口，不分配伪终端，不采用交互模式
$ ssh -TNL 8080:us.ddupan.top:8080 root@us.ddupan.top -p 1234
```