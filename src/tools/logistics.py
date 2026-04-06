from typing import Any, Dict

from src.telemetry.logger import logger


def calc_shipping(inp: str) -> Dict[str, Any]:
    """Calculate shipping cost based on weight and destination."""
    weight_kg, destination = inp.split(', ')
    weight_kg = float(weight_kg)
    base_rate = 5.0
    per_kg_rate = 2.0
    shipping_cost = base_rate + (weight_kg * per_kg_rate)

    result = {
        "weight_kg": weight_kg,
        "destination": destination,
        "shipping_cost": round(shipping_cost, 2),
        "currency": "USD",
    }
    logger.log_event("TOOL_EXECUTED", {"tool": "calc_shipping", "result": result})
    return result
