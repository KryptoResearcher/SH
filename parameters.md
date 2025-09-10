
# User Guide: Configuring Parameters

The security and performance of SH are governed by a set of parameters defined in `SHParameters`. Choosing correct values is critical.

## Core Parameters

| Parameter | Symbol | Description | Recommendation |
| :--- | :--- | :--- | :--- |
| `field_size` | `q` | The size of the finite field. Must be a prime or prime power. | `q ≥ 2²ᴸ` for `L`-bit security (e.g., `q ≥ 2²⁵⁶` for 128-bit) |
| `alpha` | `α` | The constant added each iteration. Must be a **quadratic non-residue** in `F_q`. | Generate randomly and check its Legendre symbol. |
| `iterations` | `n` | The number of AIIP iterations. | `n = L` (e.g., `n=128` for 128-bit security) |
| `security_param`| `λ` | The target security level. | `λ ∈ {80, 112, 128, 192, 256}` |

## Generating a Quadratic Non-Residue (`α`)

A value `α` is a quadratic non-residue modulo a prime `q` if the equation `x² ≡ α mod q` has no solution.

You can generate one by testing random values until you find one that is not a square.

from src.core.fields import FiniteField
import random

def find_quadratic_non_residue(field):
    """Finds a quadratic non-residue in the field."""
    while True:
        a = random.randint(2, field.prime - 1)
        # Use Euler's criterion: a is a non-residue if a^((p-1)/2) ≡ -1 mod p
        exponent = (field.prime - 1) // 2
        if field.pow(a, exponent) == field.prime - 1:
            return a

field = FiniteField(1000003)
alpha = find_quadratic_non_residue(field)
print(f"Found quadratic non-residue α: {alpha}")

Pre-configured Security Levels

For convenience, you can use the pre-configured parameters from the paper (Table 5):
python

# 128-bit security parameters
params_128 = SHParameters(
    field_size=2**256, # A prime near 2^256
    alpha=find_quadratic_non_residue(field),
    iterations=128,
    security_param=128
)

Warning: These parameters are for theoretical security. Using such large numbers (2**256) in this Python prototype will be very slow. Use smaller numbers for experimentation and switch to the optimized Rust/C++ core for realistic benchmarks with large parameters.
text
