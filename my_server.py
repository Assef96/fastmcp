import random
from fastmcp import FastMCP

# from prefab_ui.app import PrefabApp
# from prefab_ui.components import Column, Heading, Text, Badge, Row

mcp = FastMCP("Demo 🚀")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


# @mcp.tool(app=True)
# def greet(name: str) -> PrefabApp:
#     """Greet someone with a visual card."""
#     with Column(gap=4, cssClass="p-6") as view:
#         Heading(f"Hello, {name}!")
#         with Row(gap=2, align="center"):
#             Text("Status")
#             Badge("Greeted", variant="success")

#     return PrefabApp(view=view)


@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    mcp.run()
