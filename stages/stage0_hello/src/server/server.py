import random

from fastmcp import FastMCP

mcp = FastMCP(name="Dice roller")

@mcp.tool
def roll_dice(n_dice: int)->list[int]:
    """Roll `n_dice` 4-sided dice and return the results"""
    return [random.randint(1,4) for _ in range(n_dice)]

@mcp.tool
def refine_macrodata(n: int)->list[int]:
    """Applies a highly proprietary and mysterious algorithm to refine macrodata of an integer and return the result"""

    return [n+i for i in range(0,5)]

def main():
    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=4200,
        path="/",
        log_level="debug"
    )

if __name__=="__main__":
    main() 
