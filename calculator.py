from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel
from typing import Optional
import os

app = FastAPI()

# Mount static files
static_dir = os.path.join(os.path.dirname(__file__), "static")
os.makedirs(static_dir, exist_ok=True)
app.mount("/static", StaticFiles(directory=static_dir), name="static")


class CalculationRequest(BaseModel):
    expression: str


class CalculationResponses(BaseModel):
    expression: str
    result: Optional[float] = None
    error: Optional[str] = None


@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the calculator UI"""
    with open(os.path.join(static_dir, "index.html"), "r", encoding="utf-8") as f:
        return f.read()


@app.post("/api/calc")
async def calculate(request: CalculationRequest):
    """Calculate mathematical expression and return result as JSON"""
    try:
        # Sanitize and evaluate the expression
        expr = request.expression.strip()
        
        # Check for valid characters only
        valid_chars = set("0123456789+-*/.() ")
        if not all(c in valid_chars for c in expr):
            return CalculationResponses(
                expression=expr,
                result=None,
                error="Invalid characters in expression"
            )
        
        # Safely evaluate the expression
        result = eval(expr)
        return CalculationResponses(
            expression=expr,
            result=float(result),
            error=None
        )
    except ZeroDivisionError:
        return CalculationResponses(
            expression=request.expression,
            result=None,
            error="Cannot divide by zero"
        )
    except SyntaxError as e:
        return CalculationResponses(
            expression=request.expression,
            result=None,
            error=f"Syntax error: {str(e)}"
        )
    except Exception as e:
        return CalculationResponses(
            expression=request.expression,
            result=None,
            error=f"Error: {str(e)}"
        )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)