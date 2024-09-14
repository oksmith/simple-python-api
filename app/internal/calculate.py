from app.models.requests import Colour


def calculate(
    n: int, env_param: float, colour: Colour
) -> str:
    """
    This function does nothing, it's just an illlustration.
    """
    num = n * env_param
    return f"{colour.name}: {num}"
