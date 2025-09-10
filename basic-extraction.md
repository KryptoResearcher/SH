# Tutorial: Basic Extraction

This tutorial walks through the `01_basic_extraction.py` example line-by-line.

## Objective

To understand the two fundamental steps of the SH primitive:
1.  The AIIP iterative computation.
2.  The semantic mapping function `φ`.

## Code Walkthrough

### 1. Import and Setup

from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map
from src.types import SHParameters

We import the core functionality: finite field arithmetic, the AIIP function, the mapping function, and the parameter dataclass.
### 2. Initialize Parameters

params = SHParameters(
    field_size=1000003,
    alpha=5,
    iterations=10,
    security_param=80
)
field = FiniteField(params.field_size)

We set up a finite field F_1000003 and define our parameters. For this demo, we use a small field and few iterations. The value 5 is a chosen quadratic non-residue modulo 1000003.
3. Compute the AIIP Trace

input_data = 123456
trace = compute_iteration_trace(input_data, params.alpha, params.iterations, field)

This is the cryptographic core. The function calculates:
x₀ = 123456
x₁ = (123456)² + 5 mod 1000003
x₂ = (x₁)² + 5 mod 1000003
...
x₁₀ = (x₉)² + 5 mod 1000003

The trace list contains all intermediate values.
4. Apply the Semantic Map φ
python

verdict_space = ["Compliant", "Non-Compliant", "Further Investigation Needed", "Inconclusive"]
final_verdict = semantic_map(trace[-1], verdict_space, params.field_size)

The final element of the trace (trace[-1]) is mapped into the verdict_space.
The mapping is deterministic: the same final element will always produce the same verdict for a given verdict space and field size.
Exercises

    Modify the input: Change input_data to another number. Does the verdict change?

    Modify iterations: Change iterations to 5 or 15. How does the final element change?

    Expand the verdict space: Add more options to the verdict_space list. How does this affect the mapping?

text

