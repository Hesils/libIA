import math

def get_norm(v: list[float]) -> float:
    return math.sqrt(math.fsum([x * x for x in v]))


def normalize_vector(v: list[float]) -> list[float]:
    norm = get_norm(v)
    if not norm:
        return v
    return [x / norm for x in v]