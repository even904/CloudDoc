---
author: [Even]
date: [2025年09月23日]
update: [2025年09月23日]
title: [【知识框架】Docker知识体系：从基础原理到云原生生态]
tags: [Docker,容器化,镜像与容器,多架构支持,网络模式,数据管理,Docker Compose,Kubernetes,CI/CD,云原生]
---

# 主体框架
```xmind preview
xmind/知识框架/Docker知识体系全景图.xmind
```

# 应用注意

- docker engine可以处理操作系统差异，所以镜像可以相同
- docker image镜像与CPU架构强相关，例如amd64镜像不可用于arm64架构CPU
- docker 镜像中包含的是编译好的二进制程序（如 node、java、nginx），这些程序是为特定 CPU 架构编译的