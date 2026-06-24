from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Math")

@mcp.tool()
def add(a: int, b: int)-> int:
    """ _summary_
        Add 2 numbers
    """
    return a+b

@mcp.tool()
def multiply(a: int, b: int)-> int:
    """ _summary_
        Multiply 2 numbers
    """
    return a*b


if __name__ == "__main__":

    # THE stdid ARGUMENT TELLS THE SERVER TO 
    # USE STANDARD INPUT/OUTPUT  stdin and stdout, TO RECEIVE AND RESPOND TO TOOL FUNCTION CALLS
    # WE WILL GIVE THE INPUT AND OUTPUT IN TERMINAL ONLY, IT IS HELPFUL TO RUN LOCALLY
    mcp.run(transport="stdio")