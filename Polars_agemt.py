from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import Optional
import polars as pl
import schedule
from datetime import datetime
import io

app = FastAPI()


# --- Dictionary-based dynamic operations (Strategy pattern) ---
FILTER_OPERATORS = {
    "==": lambda col, val: pl.col(col) == val,
    "!=": lambda col, val: pl.col(col) != val,
    ">": lambda col, val: pl.col(col) > val,
    "<": lambda col, val: pl.col(col) < val,
    ">=": lambda col, val: pl.col(col) >= val,
    "<=": lambda col, val: pl.col(col) <= val
}

AGG_FUNCTIONS = {
    "mean": lambda col: pl.col(col).mean(),
    "sum": lambda col: pl.col(col).sum(),
    "max": lambda col: pl.col(col).max(),
    "min": lambda col: pl.col(col).min()
}


# --- Polars Expert Agent with real-time evolution capability ---
class PolarsExpertAgent:
    def __init__(self):
        self.df: Optional[pl.DataFrame] = None
        self.last_update = None
        self.knowledge_base = []

    def load_csv(self, file_bytes: bytes):
        """Load CSV data from uploaded bytes."""
        self.df = pl.read_csv(io.BytesIO(file_bytes))
        return {"message": "Data successfully loaded."}

    def show_schema(self):
        """Return the dataframe schema."""
        if self.df is None:
            raise ValueError("No data loaded.")
        return self.df.schema

    def preview_data(self, n: int = 5):
        """Return first n rows of the dataframe."""
        if self.df is None:
            raise ValueError("No data loaded.")
        return self.df.head(n)

    def filter_data(self, column: str, operator: str, value):
        """Filter dataframe using dynamic operator."""
        if self.df is None:
            raise ValueError("No data loaded.")
        if operator not in FILTER_OPERATORS:
            raise ValueError("Unsupported filter operator.")
        return self.df.filter(FILTER_OPERATORS[operator](column, value))

    def summarize(self):
        """Get dataframe summary statistics."""
        if self.df is None:
            raise ValueError("No data loaded.")
        return self.df.describe()

    def group_data(self, group_by_col: str, target_col: str, agg_func: str):
        """Perform group by with aggregation."""
        if self.df is None:
            raise ValueError("No data loaded.")
        if agg_func not in AGG_FUNCTIONS:
            raise ValueError("Unsupported aggregation function.")
        return self.df.groupby(group_by_col).agg(AGG_FUNCTIONS[agg_func](target_col))

    def scan_web_for_updates(self):
        """Simulate scanning the web for new tools or methods."""
        new_knowledge = self._mock_web_discovery()
        self.knowledge_base.extend(new_knowledge)
        self.last_update = datetime.now()

    def evolve_agent(self):
        """Perform agent self-improvement routine."""
        self.scan_web_for_updates()
        self.rewrite_logic_if_needed()

    def suggest_opportunities(self):
        """Return simulated insights based on data and trends."""
        return self._mock_insight_report()

    def schedule_updates(self):
        """Set up 6-hour auto-evolution."""
        schedule.every(6).hours.do(self.evolve_agent)

    # --- Internal mock functions to simulate external systems ---
    def _mock_web_discovery(self):
        return [
            "⚙️ New lazy loading feature released for Polars.",
            "🚀 Optimized joins using sorted keys now available."
        ]

    def rewrite_logic_if_needed(self):
        print("✅ Agent logic reviewed and updated.")

    def _mock_insight_report(self):
        return {
            "insight": "Enable lazy execution for large files.",
            "tip": "Use scan_csv() instead of read_csv() for big data pipelines."
        }


# --- Instantiate the agent ---
agent = PolarsExpertAgent()

# --- FastAPI Endpoints ---
@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    """Upload and load a CSV file into the agent."""
    try:
        content = await file.read()
        return agent.load_csv(content)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/schema/")
def get_schema():
    """Return the schema of the loaded dataset."""
    return agent.show_schema()


@app.get("/head/")
def preview_head(n: int = 5):
    """Preview the top n rows of the dataset."""
    return agent.preview_data(n).to_dicts()


@app.get("/filter/")
def filter_data(column: str, operator: str, value: str):
    """Apply a filter to the dataframe."""
    try:
        return agent.filter_data(column, operator, value).to_dicts()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/summary/")
def get_summary():
    """Get statistical summary of the dataset."""
    return agent.summarize().to_dicts()


@app.get("/groupby/")
def group_by(column: str, agg_column: str, agg_func: str):
    """Group and aggregate the dataset."""
    try:
        return agent.group_data(column, agg_column, agg_func).to_dicts()
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/opportunities/")
def profit_insights():
    """Get profit-generating suggestions."""
    return agent.suggest_opportunities()


@app.get("/update/")
def trigger_update():
    """Manually trigger agent evolution."""
    agent.evolve_agent()
    return {"status": "Agent updated", "last_update": str(agent.last_update)}
