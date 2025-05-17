from strands import tool
import math

@tool
def calculator(expression: str) -> str:
    try:
        result = eval(expression, {"__builtins__": {}, "sqrt": math.sqrt})
        return str(result)
    except Exception as e:
        return f"Calculator error: {e}"
