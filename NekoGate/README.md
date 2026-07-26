<h1 align="center">NekoGate</h1>

<p align="center"><b>自研协议内网穿透与代理管理工具</b></p>

<p align="center">Rust · React · Ant Design · Tokio · SOCKS5</p>

---

## 架构

```
┌──────────────┐     Web 面板      ┌──────────────┐
│   Browser    │◄─────────────────►│  NekoGate    │
│  (Operator)  │     管理 API      │   Server     │
└──────────────┘                   └──────┬───────┘
                                          │ 自研隧道协议
                                          ▼
                                   ┌──────────────┐
                                   │  NekoGate    │
                                   │   Client     │
                                   └──────┬───────┘
                                          │
                                          ▼
                                   内网服务 / SOCKS5
```

| 组件 | 语言 | 职责 |
|------|------|------|
| **Server** | Rust | 接入管理、隧道调度、端口转发、Web 面板与 API |
| **Client** | Rust | 出站回连、代理执行、连通性检测 |
| **Web 面板** | React | 客户端管理、在线状态、代理规则、暂停/恢复 |

## 功能

- **自研隧道协议**：client ↔ server 通信协议完全自研，不复用常见穿透 / 代理工具的协议特征；对外代理侧采用标准 SOCKS5
- **TCP 端口转发**：外部访问 server 端口 → 经隧道到达 client 侧内网服务
- **SOCKS5 出口**：client 侧标准 SOCKS5，按需动态访问目标
- **集中管理**：服务端统一配置客户端与规则；client 凭 server 地址与密钥启动
- **多客户端**：多 client 并发在线，面板查看状态 / 版本 / IP
- **暂停 / 恢复**：面板即时控制对外端口与客户端可用性
- **连通性检测**：链路异常时 client 自动退出，避免僵死连接
- **跨平台**：单一静态二进制（linux / macOS / Windows × amd64 / arm64）

## 技术栈

| 组件 | 技术 |
|------|------|
| Server / Client | Rust · Tokio · Axum |
| 前端 | React 18 · Ant Design 5 · Vite |
| 静态资源 | rust-embed |
| 代理 | SOCKS5（RFC 1928） |
| 构建 | 一键脚本 · 多目标交叉编译 |

---

<p align="center"><i>仅供授权安全测试、红队评估和安全研究教育使用</i></p>
