#!/usr/bin/env python3
"""
Example 1: Basic Extraction
Demonstrates the core AIIP iteration and semantic mapping.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.core.fields import FiniteField
from src.core.aiip import compute_iteration_trace
from src.legal.mapping import semantic_map
from src.types import SHParameters

def main():
    print("=== Example 1: Basic SH Extraction ===\n")
    
    # 1. Initialize parameters (using small values for demonstration)
    params = SHParameters(
        field_size=1000003,  # A prime number ~1e6
        alpha=5,            # A quadratic non-residue mod 1000003
        iterations=10,
        security_param=80
    )
    field = FiniteField(params.field_size)
    
    # 2. Sample input data (in practice, this would be a hash)
    input_data = 123456
    print(f"Input data (hash): {input_data}")
    print(f"Field size (q): {params.field_size}")
    print(f"Alpha (α): {params.alpha}")
    print(f"Iterations (n): {params.iterations}\n")
    
    # 3. Compute the AIIP trace
    trace = compute_iteration_trace(input_data, params.alpha, params.iterations, field)
    print(f"Final field element (fⁿ(h)): {trace[-1]}\n")
    
    # 4. Define a simple verdict space and map the final element
    verdict_space = [
        "Compliant", 
        "Non-Compliant", 
        "Further Investigation Needed",
        "Inconclusive"
    ]
    
    final_verdict = semantic_map(trace[-1], verdict_space, params.field_size)
    print(f"Mapped Verdict: '{final_verdict}'")
    print(f"Verdict Space: {verdict_space}")

if __name__ == "__main__":
    main()