from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Todo")

todos = []

@mcp.tool()
def add_task(title: str):
    todos.append(title)
    return {"status": "added", "count": len(todos)}

@mcp.tool()
def list_tasks():
    return todos

@mcp.tool()
def remove_task(title: str):
    if title in todos:
        todos.remove(title)
        return {"status": "removed"}
    return {"status": "not_found"}

if __name__ == "__main__":
    mcp.run()