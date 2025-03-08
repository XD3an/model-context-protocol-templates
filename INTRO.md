# Introduction

Model Context Protocol（MCP）是 Anthropic 於 2024 年 11 月發布的開源協定，**專為大型語言模型（Large Language Model，LLM）設計，旨在解決 AI 與外部資料源和系統連接的標準化問題**。MCP 提供了一個結構化框架，使模型能夠在對話中整合和利用外部上下文（context），從而擴展其功能並提高回應的準確性。

- https://www.anthropic.com/news/model-context-protocol

- https://modelcontextprotocol.io/introduction

### MCP 的核心目標

Anthropic 開發 MCP 的主要目的是解決 AI 系統在處理外部上下文時缺乏標準化的問題。即使是最先進的模型也受到與資料隔離的限制，無法有效存取儲存在內容儲存庫、業務工具和開發環境中的訊息。MCP 旨在替代現有的分散集成方式，提供一個單一的協定，使 AI 系統能夠更簡單、更可靠地存取所需的資料。

### MCP 的核心概念

MCP 建立在幾個關鍵概念上：

1. **上下文增強**：允許模型存取超出其訓練資料的訊息。
2. **工具整合**：提供標準化方式來與外部工具和 API 互動。
3. **結構化格式**：使用統一的格式來組織和表示額外的上下文。
4. **語義理解**：確保模型能夠正確解釋和應用提供的上下文。

### MCP 的架構與工作方式

- MCP 的架構相對簡單：開發者可以透過 **MCP 服務器（MCP Server）**公開他們的資料，或者構建連接到這些服務器的 **AI 應用程序（MCP Client）**。這種架構使資料源與 AI 系統之間能夠建立安全的雙向連接。
- 為了幫助開發者快速入門，Anthropic 提供了多個預構建的 MCP 服務器，用於連接常用的企業系統，包括 Google Drive、Slack、GitHub、Git、Postgres 和 Puppeteer 等。
    - https://github.com/modelcontextprotocol/servers

### 技術手冊與文檔

https://modelcontextprotocol.io/introduction

MCP（Model Context Protocol）官方技術文檔提供了全面的開發指南和參考資料，主要包含：

- **簡介與概念**：將 MCP 比作 AI 應用的「USB-C 接口」，標準化 AI 模型與資料源的連接方式
- **架構說明**：介紹 MCP 主機、客戶端、服務器以及與本地/遠程資料源的交互關係
- **使用者指南**：為三類使用者（服務器開發者、客戶端開發者和 Claude Desktop 用戶）提供不同的入門路徑
- **SDK 文檔**：包含 Python、TypeScript、Java 和 Kotlin 的 SDK 使用指南
- **核心功能**：詳細解釋資源、提示模板、工具、採樣和傳輸等 MCP 關鍵功能
- **實例與教程**：提供示例服務器、客戶端以及實用教程，包括使用 LLM 構建 MCP、調試技巧等
- **支持渠道**：列出不同類型問題的反饋途徑，包括 GitHub issues、討論區和郵件聯繫方式