# model-context-protocol-templates

- [Introduction](#introduction)
- [SDK](#sdk)
- [Quickstart](#quickstart)
- [Debugging & Inspection](#debugging--inspection)
  - [Debugging](#debugging)
  - [Inspector](#inspector)
    - [Inspecting servers from NPM or PyPi](#inspecting-servers-from-npm-or-pypi)
    - [Inspecting locally developed servers](#inspecting-locally-developed-servers)
- [MCP Servers](#mcp-servers)
- [Templates](#templates)
    - [**Python MCP Server Template**](#python-mcp-server-template)

## [Introduction](INTRO.md)

Model Context Protocol（MCP）是 Anthropic 於 2024 年 11 月發布的開源協定，**專為大型語言模型（Large Language Model，LLM）設計，旨在解決 AI 與外部資料源和系統連接的標準化問題**。MCP 提供了一個結構化框架，使模型能夠在對話中整合和利用外部上下文（context），從而擴展其功能並提高回應的準確性。

- https://www.anthropic.com/news/model-context-protocol

- https://modelcontextprotocol.io/introduction

    - [Why MCP?](https://modelcontextprotocol.io/introduction#why-mcp%3F)
    - [Get started](https://modelcontextprotocol.io/introduction#get-started)
    - [Tutorials](https://modelcontextprotocol.io/introduction#tutorials)
    - [Explorer MCP](https://modelcontextprotocol.io/introduction#explore-mcp)
    - ...

## SDK

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)

- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

- [Specification](https://spec.modelcontextprotocol.io/latest/)


## Quickstart

- [https://modelcontextprotocol.io/introduction#quick-starts](https://modelcontextprotocol.io/introduction#quick-starts)

## Debugging & Inspection

### [Debugging](https://modelcontextprotocol.io/docs/tools/debugging)

1. MCP Inspector

2. Claude Desktop Developer Tools

3. Server Logging

### [Inspector](https://modelcontextprotocol.io/docs/tools/inspector)

```
npx @modelcontextprotocol/inspector <command> <arg1> <arg2>
```

#### Inspecting servers from NPM or PyPi

- NPM package

    ```
    npx -y @modelcontextprotocol/inspector npx <package-name> <args>
    # For example
    npx -y @modelcontextprotocol/inspector npx server-postgres postgres://127.0.0.1/testdb
    ```

- PyPi package

    ```
    npx @modelcontextprotocol/inspector uvx <package-name> <args>
    # For example
    npx @modelcontextprotocol/inspector uvx mcp-server-git --repository ~/code/mcp/servers.git
    ```

#### Inspecting locally developed servers

- TypeScript

    ```
    npx @modelcontextprotocol/inspector node path/to/server/index.js args...
    ```

- Python

    ```
    npx @modelcontextprotocol/inspector \
        uv \
        --directory path/to/server \
        run \
        package-name \
        args...
    ```

## MCP Servers

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

## Templates

- [kirill-markin/example-mcp-server](https://github.com/kirill-markin/example-mcp-server)