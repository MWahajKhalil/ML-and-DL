from fastmcp import FastMCP

mcp= FastMCP(name = "Calculator")

@mcp.tool()
def multiply (a: float, b: float) -> float:
    """Multiplies two numbers and returns the result.
    agruments:
    a: float : first number
    b: float : second number   
    returns: float : product of a and b  
    """
    return a * b 



@mcp.tool() #decorator (means this function is a tool) is used to define a tool
def divide (a: float, b: float) -> float:
    """Divides two numbers and returns the result."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool(    #we are adding metadata to the tool using parameters of the decorator because the function name is not descriptive enough
    name ="add",
    description="Adds two numbers and returns the result.",
    tags= {"arithmetic", "addition"}  #tags for the tool

)
def add (a: float, b: float) -> float:
    """Adds two numbers and returns the result."""
    return a + b    


@mcp.tool()
def subtract (a: float, b: float) -> float:
    """Subtracts two numbers and returns the result."""
    return a - b    


if __name__ == "__main__":       #this block will only run if this file is executed directly, not when imported as a module
    mcp.run()