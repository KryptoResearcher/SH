def semantic_map(field_element: int, verdict_space: List[str], field_size: int) -> str:
    """
    Implements the semantic mapping function φ: F_q → V_J.
    φ(z) = Extract( Partition( Normalize(z) ) )

    Args:
        field_element: The element z from F_q to map.
        verdict_space: The list of possible verdicts V_J.
        field_size: The size q of the finite field.

    Returns:
        A verdict from the verdict_space.
    """
    num_verdicts = len(verdict_space)
    # Normalize: In a prime field, the element is already an integer in [0, q-1]
    normalized = field_element
    # Partition: k -> floor(k * |V_J| / q)
    index = (normalized * num_verdicts) // field_size
    # Handle edge case if field_element == q
    index = min(index, num_verdicts - 1)
    # Extract: index into the verdict space
    return verdict_space[index]