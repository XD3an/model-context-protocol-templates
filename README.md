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
    - [**Python MCP Server Template**](/templates/Python/Guideline.md)

## 👉 [Introduction](INTRO.md)

Model Context Protocol (MCP) is an open source protocol released by Anthropic in November 2024. It is designed for large language models (LLM) and aims to solve the standardization problem of connecting AI with external data sources and systems. MCP provides a structural framework that enables models to integrate and leverage external context in conversations, thereby extending their capabilities and improving the accuracy of their responses.

MCP provides the following three capabilities to extend LLM:

- **Resources** for knowledge expansion
- **Tools** calls external tools
- **Prompts** Pre-written prompts

Refer to the following:

- https://www.anthropic.com/news/model-context-protocol

- https://modelcontextprotocol.io/introduction

    - [Why MCP?](https://modelcontextprotocol.io/introduction#why-mcp%3F)
    - [Get started](https://modelcontextprotocol.io/introduction#get-started)
    - [Tutorials](https://modelcontextprotocol.io/introduction#tutorials)
    - [Explorer MCP](https://modelcontextprotocol.io/introduction#explore-mcp)
    - ...

## 👨‍💻 SDK 👩‍💻

- [Python SDK](https://github.com/modelcontextprotocol/python-sdk)

- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)

- [Java SDK](https://github.com/modelcontextprotocol/java-sdk)

- [Kotlin SDK](https://github.com/modelcontextprotocol/kotlin-sdk)

- [Specification](https://spec.modelcontextprotocol.io/latest/)


## 🔘 Quickstart

- [https://modelcontextprotocol.io/introduction#quick-starts](https://modelcontextprotocol.io/introduction#quick-starts)

## 🔍Debugging & Inspection

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

## 💻 MCP Servers

- [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

- [mcp.so](https://mcp.so/)

## 🧾 Templates

- [kirill-markin/example-mcp-server](https://github.com/kirill-markin/example-mcp-server)


### [**Python MCP Server Template**](/templates/Python/Guideline.md)

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

- **Features**
    - Resources
    - Tool
    - Prompt
    - Image
    - Context
    - ...

### [**TypeScript MCP Server Template**](/templates/TypeScript/Guideline.md)


### [**Java MCP Server Template**](/templates/Java/Guideline.md)


### [**Kotlin MCP Server Template**](/templates/Kotlin/Guideline.md)


## 🚨 MCP Security

- [InvariantLabs: MCP Security Notification Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks) : A new security issue has been identified in the MCP protocol.
    - [/security/mcp-security-demo](/security/mcp-security-demo)
        - demo1: MCP Rug Pulls
        - demo2: Shadowing Tool Descriptions

