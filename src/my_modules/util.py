from datetime import datetime

def util(input: str) -> str:
    input = add_time(input)
    return f"util: {input}"

def add_time(input: str) -> str:
    return f"{datetime.now()}: {input}"

def get_data() -> str:
    return "Return some data"