# Python MCP Template Guideline

- **Resources**

    - [https://modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)

    - [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)

- **Features**
    - Resources
    - Tool
    - Prompt
    - Image
    - Context
    - ...

## Usage

### 1. Initialization

create a uv-managed project
```bash
uv init <server-name>
cd <server-name>
```

Then add MCP to your project dependencies:

```bash
uv add "mcp[cli]"

# or 

pip install "mcp[cli]"
```

#### Running the standalone MCP development tools

```bash
uv run /path/to/server
```

### 2. Development

#### Server

The FastMCP server is your core interface to the MCP protocol. It handles connection management, protocol compliance, and message routing:

```py
# Add lifespan support for startup/shutdown with strong typing
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass

from fake_database import Database  # Replace with your actual DB type

from mcp.server.fastmcp import Context, FastMCP

# Create a named server
mcp = FastMCP("My App")

# Specify dependencies for deployment and development
mcp = FastMCP("My App", dependencies=["pandas", "numpy"])


@dataclass
class AppContext:
    db: Database


@asynccontextmanager
async def app_lifespan(server: FastMCP) -> AsyncIterator[AppContext]:
    """Manage application lifecycle with type-safe context"""
    # Initialize on startup
    db = await Database.connect()
    try:
        yield AppContext(db=db)
    finally:
        # Cleanup on shutdown
        await db.disconnect()


# Pass lifespan to server
mcp = FastMCP("My App", lifespan=app_lifespan)


# Access type-safe lifespan context in tools
@mcp.tool()
def query_db(ctx: Context) -> str:
    """Tool that uses initialized resources"""
    db = ctx.request_context.lifespan_context["db"]
    return db.query()
```

#### Resources

Resources are how you expose data to LLMs. They're similar to GET endpoints in a REST API - they provide data but shouldn't perform significant computation or have side effects:

```py

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    return "App configuration here"


@mcp.resource("users://{user_id}/profile")
def get_user_profile(user_id: str) -> str:
    """Dynamic user data"""
    return f"Profile data for user {user_id}"
```

#### Tools

Tools let LLMs take actions through your server. Unlike resources, tools are expected to perform computation and have side effects:

```py
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("My App")


@mcp.tool()
def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI given weight in kg and height in meters"""
    return weight_kg / (height_m**2)


@mcp.tool()
async def fetch_weather(city: str) -> str:
    """Fetch current weather for a city"""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://api.weather.com/{city}")
        return response.text
```

#### Prompts

Prompts are reusable templates that help LLMs interact with your server effectively:

```py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base

mcp = FastMCP("My App")


@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]
```

#### Images

FastMCP provides an `Image` class that automatically handles image data:

```py
from mcp.server.fastmcp import FastMCP, Image
from PIL import Image as PILImage

mcp = FastMCP("My App")


@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")
```

#### Context

The Context object gives your tools and resources access to MCP capabilities:

```py
from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP("My App")


@mcp.tool()
async def long_task(files: list[str], ctx: Context) -> str:
    """Process multiple files with progress tracking"""
    for i, file in enumerate(files):
        ctx.info(f"Processing {file}")
        await ctx.report_progress(i, len(files))
        data, mime_type = await ctx.read_resource(f"file://{file}")
    return "Processing complete"
```

### 3. Debugging

- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector): A tool to inspect MCP servers and clients.

#### Run with MCP Inspector

```bash
mcp dev /path/to/server

# or

npx @modelcontextprotocol/inspector \
    uv \
    --directory /path/to/server \
    run \
    <server-name> \
    args...
```

### 4. Integration

#### Claude Desktop

```bash
mcp install /path/to/server/server.py
```

#### Manual Integration

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/server",
                "run",
                "server.py"
            ]
        }
    }
}
```

## Reference

- [https://modelcontextprotocol.io/quickstart/server](https://modelcontextprotocol.io/quickstart/server)

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
