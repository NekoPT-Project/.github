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
                                          │ (TCP / TLS / WS / SSH / REALITY)
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
| **Web 面板** | React | 客户端管理、在线状态、代理规则实时编辑、暂停/恢复 |

## 功能

- **自研隧道协议**：client ↔ server 通信协议完全自研，不复用常见穿透 / 代理工具的协议特征；对外代理侧采用标准 SOCKS5
- **五种流量伪装**：裸 TCP / TLS（伪装 HTTPS）/ WebSocket（伪装实时应用）/ 真 SSH 协议外壳 / REALITY（伪装成访问真实网站的 TLS1.3，主动探测落到真实站点）——按场景选，抗被动流量分析与主动探测
- **TLS 钉扎**：client 可钉扎 server 证书指纹，抵抗企业 SSL 解密网关 MITM
- **TCP 端口转发**：外部访问 server 端口 → 经隧道到达 client 侧内网服务
- **SOCKS5 出口**：client 侧标准 SOCKS5，按需动态访问目标
- **集中管理**：服务端统一配置客户端与规则；client 凭 server 地址与密钥零配置启动
- **Web 面板实时编辑**：代理规则增删改实时下发到在线 client，无需重连
- **多客户端**：多 client 并发在线，面板查看状态 / 版本 / IP
- **暂停 / 恢复**：面板即时控制对外端口与客户端可用性
- **自动重连**：链路异常时双向检测（90s 不活跃超时），client 自动重连 / server 自动释放
- **跨平台**：单一静态二进制（Linux / macOS / Windows × amd64 / arm64）

## 技术栈

| 组件 | 技术 |
|------|------|
| Server / Client | Rust · Tokio · Axum |
| TLS 伪装 | rustls + rcgen（自签证书，CN 随机伪装厂商） |
| WebSocket 伪装 | tokio-tungstenite |
| SSH 外壳 | russh（完整 SSH 协议栈） |
| REALITY 伪装 | 伪装成访问真实网站的 TLS1.3（主动探测被引导到真实站点） |
| 前端 | React 18 · Ant Design 5 · Vite |
| 静态资源 | rust-embed |
| 代理 | SOCKS5（RFC 1928） |
| 持久化 | SQLite（rusqlite） |

---

<p align="center"><i>仅供授权安全测试、红队评估和安全研究教育使用</i></p>
