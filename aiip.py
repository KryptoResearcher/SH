from .fields import FiniteField

def compute_iteration_trace(start: int, alpha: int, iterations: int, field: FiniteField) -> List[int]:
    """
    Computes the AIIP trace: [x, f(x), f(f(x)), ..., fⁿ(x)]
    where f(x) = x² + α.

    Args:
        start: The initial field element (x).
        alpha: The constant α (quadratic non-residue).
        iterations: The number of iterations n.
        field: An instance of FiniteField.

    Returns:
        The list of field elements representing the computation trace.
    """
    trace = [start]
    current = start

    for _ in range(iterations):
        # Calculate next value: current² + α mod q
        squared = field.mul(current, current)
        next_val = field.add(squared, alpha)
        trace.append(next_val)
        current = next_val

    return trace