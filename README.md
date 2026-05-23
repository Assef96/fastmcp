# FastMCP Demo 🚀

A demonstration of [FastMCP](https://github.com/mcp-rs/fastmcp) - a Python framework for building Model Context Protocol (MCP) servers with an easy, intuitive API.

## Project Overview

This project showcases FastMCP by implementing a simple server with three tools that can be called via the MCP protocol:

- **`add(a, b)`** - Add two numbers
- **`roll_dice(n_dice)`** - Roll n 6-sided dice and return results
- **`greet(name)`** - Generate a visual greeting card with status badge

## Features

- 🎯 Simple tool definitions using Python decorators
- 🎨 UI components with [PrefabUI](https://github.com/prefab-ai/prefab-ui) for rich visualizations
- 🔌 Easy client-server communication over HTTP

## Getting Started

### Installation

1. Start the MCP server:
   ```bash
   python my_server.py
   ```
   The server runs on `http://localhost:8000/mcp` by default.

2. In another terminal, run the client:
   ```bash
   python my_client.py
   ```

## Integration with Claude Desktop

To use this with Claude Desktop:
```bash
fastmcp install claude-desktop my_server.py
```

## Project Structure

- `my_server.py` - FastMCP server with tool definitions
- `my_client.py` - Example client that calls server tools
