---
author: [Even]
date: [2025年10月13日]
update: [2025年10月13日]
title: [【工业互联网】1 Kubernetes(k8s)容器编排系统]
tags: [5G,k8s,容器,边缘计算,网络通信优化]
---

k8s核心概念树状图

``` md
Kubernetes (k8s)
│
├── **核心对象 (Core Objects)**
│   │
│   ├── Pod
│   │   └── Container
│   │       └── Image
│   │
│   ├── Node
│   │   ├── Master Node (Control Plane)
│   │   └── Worker Node
│   │
│   ├── Namespace
│   │
│   ├── Service
│   │   └── ClusterIP / NodePort / LoadBalancer
│   │
│   └── Label & Selector
│
├── **工作负载 (Workload Resources)**
│   │
│   ├── Deployment
│   │   └── ReplicaSet
│   │
│   ├── StatefulSet
│   │
│   ├── DaemonSet  ←───────────────────────────────────────┐
│   │                                                       │
│   ├── Job / CronJob                                       │
│   │                                                       │
│   └── ReplicaSet                                          │
│                                                           │
├── **配置与存储 (Configuration & Storage)**                │
│   │                                                       │
│   ├── ConfigMap                                           │
│   │                                                       │
│   ├── Secret                                              │
│   │                                                       │
│   ├── PersistentVolume (PV)                               │
│   │                                                       │
│   └── PersistentVolumeClaim (PVC)                         │
│                                                           │
├── **网络 (Networking)**                                   │
│   │                                                       │
│   ├── Ingress                                             │
│   │                                                       │
│   └── NetworkPolicy                                       │
│                                                           │
├── **安全 (Security)**                                     │
│   │                                                       │
│   ├── ServiceAccount                                      │
│   │                                                       │
│   ├── Role / ClusterRole                                  │
│   │                                                       │
│   └── RoleBinding / ClusterRoleBinding                    │
│                                                           │
└── **扩展与自定义 (Extensibility & Custom Resources)**     │
    │                                                       │
    ├── Custom Resource Definition (CRD) ←──────────────────┤
    │                                                       │
    └── Custom Resource (CR)                                │
        │                                                   │
        └── **Operator** (基于 CRD + 控制器模式实现) ────────┘
```