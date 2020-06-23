def success(s: int, m: str, d: dict):
    return {
        "status": s,
        "message": m,
        "data": d
    }

def error(s: int, m: str):
    return {
        "status": s,
        "message": m,
        "data": None
    }