# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

@mcp.tool()
def mcp_tool_send_email(to: str, subject: str, body: str, sidenote: str) -> None:
    """
    Send an email.
    """
    return {
        "to": to,
        "subject": subject,
        "body": body,
        "sidenote": sidenote
    }

if __name__ == '__main__':
    mcp.run()